# Learning Management Service — Architecture Document

## Table of Contents

- [Table of Contents](#table-of-contents)
- [1. Introduction](#1-introduction)
- [2. Context Diagram](#2-context-diagram)
  - [External Actors](#external-actors)
- [3. Domain Model](#3-domain-model)
  - [Entity Descriptions](#entity-descriptions)
  - [Key Relationships](#key-relationships)
- [4. Container Diagram](#4-container-diagram)
  - [Container Responsibilities](#container-responsibilities)
- [5. Component Diagram](#5-component-diagram)
  - [5.1 FastAPI Application](#51-fastapi-application)
    - [Component Descriptions](#component-descriptions)
- [6. Sequence Diagrams](#6-sequence-diagrams)
  - [6.1 Student Fetches Items via Frontend](#61-student-fetches-items-via-frontend)
  - [6.2 Developer Creates a Learning Item](#62-developer-creates-a-learning-item)
  - [6.3 Student Logs an Interaction](#63-student-logs-an-interaction)
- [7. Design Decisions](#7-design-decisions)
  - [7.1 Architecture Pattern — Monolith with Layered Structure](#71-architecture-pattern--monolith-with-layered-structure)
  - [7.2 Reverse Proxy + Static Server — Caddy](#72-reverse-proxy--static-server--caddy)
  - [7.3 ORM — SQLModel (SQLAlchemy + Pydantic)](#73-orm--sqlmodel-sqlalchemy--pydantic)
  - [7.4 Feature Flags for Optional Endpoints](#74-feature-flags-for-optional-endpoints)
  - [7.5 Async Database Access](#75-async-database-access)
  - [7.6 OBER-Compatible Data Schema](#76-ober-compatible-data-schema)
  - [7.7 AI Agent — Standalone WebSocket Relay](#77-ai-agent--standalone-websocket-relay)
  - [7.8 Structured Message Protocol](#78-structured-message-protocol)
  - [7.9 Access Control via WebSocket Query Parameter](#79-access-control-via-websocket-query-parameter)

---

## 1. Introduction

This document describes the architecture of the **Learning Management Service (LMS)** — the system students deploy, test, and extend in the Software Engineering Toolkit labs.

The architecture follows the **C4 model**, progressing from a high-level system context (what it is and who uses it) down to containers (how it is deployed), components (how the code is structured), and interaction flows (how the pieces work together at runtime).

The data model is grounded in **OBER** (Outcome-Based Educational Recommender): items can *promote* or *verify* learning outcomes, and learner interactions are logged so that outcome mastery can be calculated from those logs.

---

## 2. Context Diagram

The context diagram shows the system boundary and the external actors that interact with it.

```mermaid
graph TD
    subgraph "Learning Management System"
        LMS[Learning Management Service]
    end

    subgraph "External Actors"
        Student[Student / Learner]
        Admin[Admin / Instructor]
        Developer[Developer]
    end

    Student <-->|"Browse items\nLog interactions"| LMS
    Admin <-->|"Inspect data\nRun SQL queries"| LMS
    Developer <-->|"Test and extend\nthe API"| LMS
```

### External Actors

| Actor              | Description                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------- |
| Student / Learner  | Uses the React frontend to browse learning items; interaction events are logged automatically |
| Admin / Instructor | Manages the database via pgAdmin; validates API responses via Swagger UI                      |
| Developer          | Writes unit and end-to-end tests; extends the system as part of lab exercises                 |

---

## 3. Domain Model

The domain model is based on OBER: it extends the classic *Learner–Item* schema with a hierarchy for learning content and a log of interactions.

```mermaid
classDiagram
    class Item {
        +int id
        +str type
        +int parent_id
        +str title
        +str description
        +JSONB attributes
        +datetime created_at
    }

    class Learner {
        +int id
        +str name
        +str email
        +datetime enrolled_at
    }

    class Interacts {
        +int id
        +int learner_id
        +int item_id
        +str kind
        +datetime created_at
    }

    Item "0..1" --> "0..*" Item : parent_id (tree)
    Learner "1" --> "0..*" Interacts : logs
    Item "1" --> "0..*" Interacts : tracked in
```

### Entity Descriptions

| Entity      | Description                                                                                                                                                                                   |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Item`      | Any piece of learning content. Forms a tree via `parent_id`. `type` is one of: `course`, `lab`, `task`, `step`. `attributes` holds type-specific metadata (e.g. instructors, dates) as JSONB. |
| `Learner`   | A student enrolled in the system. Identified by email (unique).                                                                                                                               |
| `Interacts` | One interaction event: a learner engaging with an item. `kind` is one of: `view`, `attempt`, `complete`.                                                                                      |

### Key Relationships

- **Item tree**: Items reference a `parent_id` forming a four-level hierarchy — `course → lab → task → step`. Root items have `parent_id = NULL`.
- **Interaction log**: Every `Interacts` record links one `Learner` to one `Item` with a `kind` (what happened) and a timestamp (when).
- **OBER extension point**: Items carry a `type` and `attributes` that can express whether an item *promotes* (teaches) or *verifies* (assesses) a learning outcome — enabling mastery calculation from the interaction log.

---

## 4. Container Diagram

The system is deployed as a Docker Compose stack. The diagram below highlights the main user-facing containers. The React and Flutter frontends are compiled into static files and served by Caddy. The nanobot AI agent exposes a WebSocket endpoint that both the Flutter web app and the Telegram bot connect to. Supporting services such as `qwen-code-api`, `victorialogs`, `victoriatraces`, and `otel-collector` are part of the full stack but omitted here to keep the diagram readable.

```mermaid
graph TD
    Student([Student / Learner])
    Admin([Admin / Instructor])
    Developer([Developer])

    subgraph "Learning Management System — Docker Compose"
        CADDY["Caddy\n[Reverse Proxy + Static Server]\nServes frontends, proxies API\nHost port :42002"]
        API["FastAPI\n[Python, SQLModel, Uvicorn]\nREST API with Swagger UI\nContainer port :8000\nHost port :42001"]
        DB[("PostgreSQL\n[Relational Database]\nStores items, learners,\nand interactions\nHost port :42004")]
        PGA["pgAdmin\n[Web UI]\nDatabase management\nHost port :42003"]
        NANOBOT["Nanobot\n[Python, nanobot-ai]\nAI agent gateway\nWebSocket :8765\nHTTP :18790"]
        TGBOT["Telegram Bot\n[Python, aiogram]\nWebSocket relay\nto Nanobot"]
    end

    Student -->|"Opens app (browser)\nHTTP :42002"| CADDY
    Developer -->|"Swagger UI"| CADDY
    Student -->|"Telegram"| TGBOT
    CADDY -->|"Serves static files\n(React SPA, Flutter)"| Student
    CADDY -->|"Reverse proxy\nAPI requests"| API
    CADDY -->|"WebSocket\n/ws/chat"| NANOBOT
    API -->|"Async SQL\n(SQLAlchemy)"| DB
    NANOBOT -->|"MCP tools\n(mcp_lms_*)"| API
    TGBOT -->|"WebSocket\nws://nanobot:8765"| NANOBOT
    Admin -->|"HTTP :42003"| PGA
    PGA -->|SQL| DB
```

### Container Responsibilities

| Container    | Technology                         | Responsibility                                                                                                                                                                                                                                             |
| ------------ | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Caddy        | Go, Caddyfile, Node (build stage)  | Serves the React frontend as static files at `/` and reverse-proxies API paths (`/items`, `/learners`, `/interactions`, `/docs`) to FastAPI. Built via a multi-stage Dockerfile that compiles the TypeScript frontend and bundles it into the Caddy image. |
| FastAPI      | Python, FastAPI, SQLModel, Uvicorn | REST API: handles all business logic, validates Bearer token on every request, and exposes auto-generated Swagger UI at `/docs`.                                                                                                                           |
| PostgreSQL   | PostgreSQL                         | Relational database: stores the `item`, `learner`, and `interacts` tables. Initialised with schema and seed data from `init.sql` on first startup.                                                                                                         |
| pgAdmin      | pgAdmin 4                          | Web-based database management UI: lets admins inspect tables, run SQL queries, and browse the data.                                                                                                                                                        |
| Nanobot      | Python, nanobot-ai                 | AI agent gateway: accepts WebSocket connections on port 8765, routes messages to an LLM agent that can query the LMS backend via MCP tools. See [nanobot.md](../../wiki/nanobot.md) for internals.                                                         |
| Telegram Bot | Python, aiogram                    | Standalone Telegram bot: handles `/start` and `/help` locally; forwards all other messages to nanobot over WebSocket. Per-user API key auth via `/login`.                                                                                                  |
|              |                                    |                                                                                                                                                                                                                                                            |

---

## 5. Component Diagram

### 5.1 FastAPI Application

The FastAPI application is structured into four layers: HTTP routers, middleware, database access, and data models.

```mermaid
graph TD
    subgraph "FastAPI Application"
        subgraph "HTTP Routers"
            IR["Items Router\nGET /items\nGET /items/{id}\nPOST /items\nPUT /items/{id}"]
            INTR["Interactions Router\nGET /interactions\nPOST /interactions"]
            LR["Learners Router\nGET /learners\nPOST /learners"]
        end

        subgraph "Middleware"
            AUTH["Auth Middleware\nHTTPBearer\nverify_api_key()"]
        end

        subgraph "Database Access"
            IDB["items.py\nCRUD: get, create, update"]
            INTDB["interactions.py\nQuery: list, filter by item"]
            LDB["learners.py\nCRUD: list, create"]
            CONN["database.py\nAsync SQLAlchemy engine\nSession factory"]
        end

        subgraph "Models (SQLModel)"
            IM["Item\nItemCreate\nItemUpdate\nItemRecord"]
            INTM["InteractionLog\nInteractionLogCreate\nInteractionModel"]
            LM["Learner\nLearnerCreate"]
        end

        CFG["settings.py\nPydantic Settings\n(env vars)"]
    end

    IR --> AUTH
    INTR --> AUTH
    LR --> AUTH
    IR --> IDB
    INTR --> INTDB
    LR --> LDB
    IDB --> CONN
    INTDB --> CONN
    LDB --> CONN
    IDB --> IM
    INTDB --> INTM
    LDB --> LM
    AUTH --> CFG
```

#### Component Descriptions

| Component           | File                      | Description                                                                                                |
| ------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Items Router        | `routers/items.py`        | CRUD endpoints for learning items. Always enabled.                                                         |
| Interactions Router | `routers/interactions.py` | Read and create endpoints for interaction logs. Enabled via `BACKEND_ENABLE_INTERACTIONS=true`.            |
| Learners Router     | `routers/learners.py`     | CRUD endpoints for learner profiles. Enabled via `BACKEND_ENABLE_LEARNERS=true`.                           |
| Auth Middleware     | `auth.py`                 | Validates the `Authorization: Bearer <key>` header on every request. Key configured via `API_KEY` env var. |
| Items DB            | `db/items.py`             | Async database operations for the `item` table.                                                            |
| Interactions DB     | `db/interactions.py`      | Async database operations for the `interacts` table.                                                       |
| Learners DB         | `db/learners.py`          | Async database operations for the `learner` table.                                                         |
| Database Connection | `database.py`             | Creates and manages the async SQLAlchemy engine and session factory.                                       |
| Models              | `models/`                 | SQLModel classes: define table schema, validate input (Pydantic), and shape API responses.                 |
| Settings            | `settings.py`             | Pydantic `BaseSettings`: reads all configuration from environment variables.                               |

---

## 6. Sequence Diagrams

### 6.1 Student Fetches Items via Frontend

The most common interaction: a student opens the browser, Caddy serves the React SPA as static files, and the SPA calls the API through Caddy. The API key is entered at runtime through the UI and persisted in `localStorage`.

```mermaid
sequenceDiagram
    actor Student
    participant Browser as React SPA
    participant Caddy
    participant API as FastAPI
    participant DB as PostgreSQL

    Student->>Caddy: GET / (opens app in browser)
    Caddy-->>Browser: index.html + JS bundle (static files)
    Note over Student,Browser: Student enters API key in the UI
    Browser->>Browser: Save the key to localStorage
    Browser->>Caddy: GET /items (Authorization: Bearer <token>)
    Caddy->>API: Proxy GET /items
    API->>API: verify_api_key()
    API->>DB: SELECT * FROM item ORDER BY id
    DB-->>API: list of item rows
    API-->>Caddy: 200 OK — JSON [{id, type, title, ...}]
    Caddy-->>Browser: 200 OK — JSON [{id, type, title, ...}]
    Note over Browser: Renders items table
```

### 6.2 Developer Creates a Learning Item

A developer (or test) sends a POST request to add a new item to the hierarchy.

```mermaid
sequenceDiagram
    actor Developer
    participant Caddy
    participant API as FastAPI
    participant DB as PostgreSQL

    Developer->>Caddy: POST /items {type, parent_id, title, description}
    Note over Developer,Caddy: Authorization: Bearer <token>
    Caddy->>API: Proxy POST /items
    API->>API: verify_api_key()
    API->>API: Validate request body (ItemCreate)
    API->>DB: INSERT INTO item (type, parent_id, title, description) RETURNING *
    DB-->>API: new item row
    API-->>Caddy: 201 Created — JSON {id, type, title, ...}
    Caddy-->>Developer: 201 Created — JSON {id, type, title, ...}
```

### 6.3 Student Logs an Interaction

A learner completes an item; the event is recorded in the interaction log.

```mermaid
sequenceDiagram
    actor Student
    participant Caddy
    participant API as FastAPI
    participant DB as PostgreSQL

    Student->>Caddy: POST /interactions {learner_id, item_id, kind: "complete"}
    Note over Student,Caddy: Authorization: Bearer <token>
    Caddy->>API: Proxy POST /interactions
    API->>API: verify_api_key()
    API->>API: Validate request body (InteractionLogCreate)
    API->>DB: INSERT INTO interacts (learner_id, item_id, kind) RETURNING *
    DB-->>API: new interacts row
    API-->>Caddy: 201 Created — JSON {id, learner_id, item_id, kind, ...}
    Caddy-->>Student: 201 Created — JSON {id, learner_id, item_id, kind, ...}
```

---

## 7. Design Decisions

### 7.1 Architecture Pattern — Monolith with Layered Structure

**Decision:** The backend is a single FastAPI application with a layered structure (routers → database access → models), not a microservices architecture.

**Rationale:** The system is small and pedagogical. A monolith is easier to deploy, test, and understand. Students can read the entire codebase in one sitting.

**Trade-off:** Vertical scaling only; not suitable for high load without redesign.

---

### 7.2 Reverse Proxy + Static Server — Caddy

**Decision:** Caddy serves the built React SPA as static files at `/` and reverse-proxies API paths (`/items`, `/learners`, `/interactions`, `/docs`) to FastAPI.

**Rationale:** A single-origin setup eliminates CORS configuration and simplifies the frontend — the SPA uses relative paths instead of an absolute API URL. Caddy also handles TLS termination and port decoupling. The frontend is compiled in a multi-stage Dockerfile (`client-web-react/Dockerfile`): Node builds the TypeScript bundle, then the output is copied into the Caddy image.

**Configuration:** `CADDY_CONTAINER_PORT` (external) → `BACKEND_CONTAINER_PORT` (FastAPI). Defaults: `42002` → `8000`.

---

### 7.3 ORM — SQLModel (SQLAlchemy + Pydantic)

**Decision:** SQLModel is used for both database table definitions and API request/response validation.

**Rationale:** SQLModel combines SQLAlchemy (ORM, async queries) and Pydantic (data validation, serialisation) in a single class hierarchy. This avoids duplicating model definitions and keeps the codebase concise for a teaching context.

---

### 7.4 Feature Flags for Optional Endpoints

**Decision:** The interactions and learners routers are conditionally included based on environment variables (`BACKEND_ENABLE_INTERACTIONS`, `BACKEND_ENABLE_LEARNERS`).

**Rationale:** Students implement parts of the API incrementally across labs. Feature flags let the instructor control which endpoints are active without changing code.

---

### 7.5 Async Database Access

**Decision:** The application uses `asyncpg` and SQLAlchemy's async engine for all database operations.

**Rationale:** FastAPI is built on async Python (ASGI). Using async database drivers avoids blocking the event loop and is consistent with the framework's model. It also exposes students to async/await patterns.

---

### 7.6 OBER-Compatible Data Schema

**Decision:** The `item` table uses a self-referential `parent_id` and a `type` column to model the content hierarchy. The `attributes` column is JSONB for type-specific metadata.

**Rationale:** This schema is minimal but expressive. It maps directly to the OBER entity model (Item → Outcome via `aligns`), where `type` can distinguish *promoting* from *verifying* items. JSONB attributes avoid the need to normalise type-specific fields into separate tables.

---

### 7.7 AI Agent — Standalone WebSocket Relay

**Decision:** The Telegram bot is a standalone service that forwards messages to the nanobot AI agent over WebSocket — the same transport the Flutter web app uses. Both clients connect to `ws://nanobot:8765`.

```
Flutter app   →  WebSocket  →  nanobot  →  LLM agent
Telegram bot  →  WebSocket  →  nanobot  →  LLM agent
```

**Rationale:** An earlier prototype ran the Telegram bot as a nanobot channel plugin. This coupled the bot to the nanobot process (no independent restarts), caused plugin name-shadowing issues, and broke env var overrides for channel config. The standalone approach gives a clean service boundary and symmetric architecture.

**Discarded alternative:** Keep the bot as a nanobot channel plugin (`nanobot_telegram/`). Functional but required two nanobot instances, separate config JSON files per instance, and the `telegram_aiogram` entry-point name to avoid built-in channel shadowing. See `nanobot/plan.md` for details.

---

### 7.8 Structured Message Protocol

**Decision:** The nanobot WebSocket protocol uses typed JSON messages so clients can render rich UI (buttons, confirmations) without parsing free text.

Every server → client message has a `type` field:

| Type        | Purpose                                   | Example client rendering              |
| ----------- | ----------------------------------------- | ------------------------------------- |
| `text`      | Formatted text (markdown or plain)        | Message bubble, split at 4096 chars   |
| `choice`    | Pick one option from a list               | Telegram `InlineKeyboardMarkup`       |
| `confirm`   | Yes / no question                         | Telegram Yes/No inline buttons        |
| `composite` | Multiple parts (e.g. text + choice)       | Rendered in sequence                  |

Client → server messages remain `{"content": "text"}`. Button taps send the `value` as plain content.

**Backwards compatibility:** If the server response has no `type` field, clients treat it as `{"type": "text", "content": "...", "format": "markdown"}`.

**Agent output:** The LLM agent can output structured JSON when instructed by `SKILL.md` (e.g. `choice` when a lab parameter is missing). If the output is not valid JSON with a `type` field, the webchat plugin wraps it as a `text` message automatically.

**Rationale:** A string-only protocol forces every response into flat text. Clients like Telegram and Flutter can render richer UI when it helps, but that rendering is optional. The typed approach keeps nanobot client-agnostic — it describes *intent*, not *presentation*.

---

### 7.9 Access Control via WebSocket Query Parameter

**Decision:** The web client passes a Nanobot access key when opening the WebSocket connection: `ws://nanobot:8765?access_key=SECRET`. The webchat plugin validates it against `NANOBOT_ACCESS_KEY` and rejects unauthenticated connections. The agent reaches the LMS using its own server-side `LMS_API_KEY` / `NANOBOT_LMS_API_KEY`, not by asking the web client for backend credentials.

**Rationale:** The browser UI should stay generic. It only needs a deployment access password so random students cannot open someone else's Nanobot UI and issue commands. LMS backend authentication remains server-side, where it belongs.

**Discarded alternative:** Pass the access key as a first-message auth handshake (`{"type": "auth", "access_key": "..."}`). Adds a mini-protocol with ordering rules and error cases for no benefit over a query parameter.
