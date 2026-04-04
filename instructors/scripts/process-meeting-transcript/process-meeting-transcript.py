import argparse
import json
from pathlib import Path
from pydantic import BaseModel


class InputSentence(BaseModel):
    speaker: str
    text: str
    start: int
    end: int
    confidence: float


class SentenceEntry(BaseModel):
    text: str
    start: int
    end: int
    confidence: float


class SpeakerGroup(BaseModel):
    speaker: str
    sentences: list[SentenceEntry]


class TranscriptData(BaseModel):
    sentences: list[InputSentence]


def format_ts(ms: int) -> str:
    total_sec = ms // 1000
    minutes, seconds = divmod(total_sec, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


parser = argparse.ArgumentParser()
parser.add_argument("directory", nargs="?", default=".")
parser.add_argument(
    "--merge",
    action="append",
    default=[],
    metavar="X=Y",
    help="Treat Speaker X as Speaker Y (e.g. --merge C=B)",
)
args = parser.parse_args()

speaker_map: dict[str, str] = {}
for m in args.merge:
    src, _, dst = m.partition("=")
    if not dst:
        parser.error(f"Invalid --merge value '{m}', expected format X=Y")
    speaker_map[src.strip()] = dst.strip()

directory = Path(args.directory)
input_file = directory / "sentences.json"

with open(input_file) as f:
    data = TranscriptData.model_validate(json.load(f))

groups: list[SpeakerGroup] = []
current_speaker: str | None = None
for s in data.sentences:
    speaker = speaker_map.get(s.speaker, s.speaker)
    entry = SentenceEntry(
        text=s.text, start=s.start, end=s.end, confidence=s.confidence
    )
    if speaker == current_speaker:
        groups[-1].sentences.append(entry)
    else:
        groups.append(SpeakerGroup(speaker=speaker, sentences=[entry]))
        current_speaker = speaker

with open(directory / "transcript-by-speaker.json", "w", encoding="utf-8") as f:
    f.write(json.dumps([g.model_dump() for g in groups], ensure_ascii=False, indent=4))

with open(directory / "transcript-by-speaker.txt", "w", encoding="utf-8") as out:
    for group in groups:
        line = f"Speaker {group.speaker}: {len(group.sentences)} sentence(s)\n"
        print(line, end="")
        out.write(line)
        for s in group.sentences:
            line = f"  [{format_ts(s.start)}] {s.text}\n"
            print(line, end="")
            out.write(line)
        out.write("\n")
