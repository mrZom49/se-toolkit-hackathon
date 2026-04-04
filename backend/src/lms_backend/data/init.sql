-- Learning Management Service — Database Initialization
-- This script runs automatically on the first start of the PostgreSQL container.
-- Tables start empty — all data is populated via the ETL pipeline.

-- Item: learning materials organized as a tree (labs → tasks).
-- The tree structure uses the adjacency list pattern (parent_id).
-- Type-specific attributes are stored in a JSONB column.
CREATE TABLE IF NOT EXISTS item (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50) NOT NULL DEFAULT 'step',
    parent_id INTEGER REFERENCES item(id),
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    attributes JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Learner: students identified by anonymized external IDs
CREATE TABLE IF NOT EXISTS learner (
    id SERIAL PRIMARY KEY,
    external_id VARCHAR(255) NOT NULL UNIQUE,
    student_group VARCHAR(255) NOT NULL DEFAULT '',
    enrolled_at TIMESTAMP DEFAULT NULL
);

-- Interacts: records of learners interacting with items (check submissions)
CREATE TABLE IF NOT EXISTS interacts (
    id SERIAL PRIMARY KEY,
    external_id INTEGER UNIQUE,
    learner_id INTEGER NOT NULL REFERENCES learner(id),
    item_id INTEGER NOT NULL REFERENCES item(id),
    kind VARCHAR(50) NOT NULL,
    score DOUBLE PRECISION,
    checks_passed INTEGER,
    checks_total INTEGER,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
