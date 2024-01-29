"""""Manipulate sequence files and store sequence information.""" ''
from __future__ import annotations

from typing import Generator, Iterable
import sys


class SequenceRecord:
    """Store and manipulate sequence information."""

    def __init__(
        self,
        sequence: str,
        description: str,
        quality: str | None = None,
        encoding: str | None = None,
    ) -> None:
        self.sequence = sequence
        self.description = description
        if quality is None:
            self.quality = ''
        else:
            self.quality = quality
        if encoding is None:
            self.encoding = 'phred33'
        else:
            self.encoding = encoding
        self.name = self.description[1:].split()[0]

    def get_quality_scores(self) -> list[int]:
        """Calculate quality scores from quality string.

        Returns:
            list[int]: All quality scores as integers
        """
        encoding_to_int = {'phred33': 33, '33': 33, 'phred64': 64, '64': 64}
        return [ord(i) - encoding_to_int[self.encoding] for i in self.quality]

    def transcribe(self, reverse: bool = False) -> SequenceRecord:
        """Transcribe sequence. [UNDER CONSTRUCTION]

        Args:
            reverse (bool, optional): Whether to reverse transcribe
            RNA sequence to DNA. Defaults to False.

        Returns:
            SequenceRecord: Object containing transcribed sequence
        """
        if reverse:
            return SequenceRecord('', '')
        return SequenceRecord('', '')


class _SequenceFileReader:
    def __init__(self, path: str, encoding: str | None = None) -> None:
        self.path = path
        self.encoding = encoding
        self.sequence_count = 0

    def set_sequence_count(self) -> None:
        assert hasattr(
            self, 'stream'
        ), "Need to open file stream by running inside of 'with' block"
        for line in self.stream:
            if line.startswith('>'):
                self.sequence_count += 1
        self.stream.seek(0)

    def check_format(self) -> None:
        assert self.stream.readline().startswith('>'), 'File is not fasta/fastq format.'
        self.stream.seek(0)

    def __enter__(self):
        if self.path == '-':
            self.stream = sys.stdin
        else:
            self.stream = open(self.path, 'r', encoding='UTF-8')
        self.check_format()
        return self

    def __exit__(self, exc_type: type, exc_value: int, traceback: str) -> None:  # type: ignore
        self.stream.close()


class FastaReader:
    """Read fasta files"""

    def __init__(self, path: str, **kwargs: str) -> None:
        self.reader = _SequenceFileReader(path)
        self._last_header = ''

    def parse(self) -> Generator[SequenceRecord, None, None]:
        """Parse entire fasta file for sequences.

        Raises:
            AttributeError: File stream is not opened

        Yields:
            Generator[SequenceRecord, None, None]: Iterator containing sequences
        records from file
        """
        assert hasattr(
            self.reader, 'stream'
        ), "Need to open file stream by running inside of 'with' block"
        header = self.reader.stream.readline().rstrip()
        sequence = ''
        self.reader.sequence_count = 1
        for line in self.reader.stream:
            if line.startswith('>'):
                yield SequenceRecord(sequence, header)
                header = line.rstrip()
                sequence = ''
                self.reader.sequence_count += 1
            else:
                sequence += line.rstrip()
        yield SequenceRecord(sequence, header)

    def read_sequence(self) -> SequenceRecord:
        """Parse fasta file and return next sequence as a
        SequenceRecord object"""
        if self._last_header == '':
            header = self.reader.stream.readline().rstrip()
        else:
            header = self._last_header
        if not header.startswith('>'):
            raise ValueError("Line does not start with '>'. Reset file stream")
        sequence = self.reader.stream.readline().rstrip()
        for line in self.reader.stream:
            if line.startswith('>'):
                self._last_header = line.rstrip()
                return SequenceRecord(sequence, header)
            sequence += line.rstrip()
        return SequenceRecord(sequence, header)

    def __enter__(self) -> FastaReader:
        self.reader = self.reader.__enter__()
        return self

    def __exit__(self, exc_type: type, exc_value: int, traceback: str) -> None:  # type: ignore
        self.reader.__exit__(exc_type, exc_value, traceback)


class FastqReader:
    """Read fastq files"""

    def __init__(self, path: str, encoding: str) -> None:
        self.reader = _SequenceFileReader(path, encoding)
        self._last_header = ''

    def parse(self) -> Generator[SequenceRecord, None, None]:
        """Parse fastq file and return iterator of SequenceRecord objects."""
        assert hasattr(
            self.reader, 'stream'
        ), "Need to open file stream by running inside of 'with' block"
        header = self.reader.stream.readline().rstrip()
        sequence = ''
        quality = ''
        sequence_flag = True
        self.reader.sequence_count = 1
        for line in self.reader.stream:
            if line.startswith('>'):  # Header line
                yield SequenceRecord(sequence, header, quality, self.reader.encoding)
                header = line.rstrip()
                sequence = ''
                quality = ''
                self.reader.sequence_count += 1
            elif line.startswith('+'):  # Spacer line
                sequence_flag = False
            else:
                if sequence_flag:
                    sequence += line.rstrip()
                else:
                    quality += line.rstrip()
        yield SequenceRecord(sequence, header, quality, self.reader.encoding)

    def __enter__(self) -> FastqReader:
        self.reader = self.reader.__enter__()
        return self

    def __exit__(self, exc_type: type, exc_value: int, traceback: str) -> None:  # type: ignore
        self.reader.__exit__(exc_type, exc_value, traceback)


class _SequenceFileWriter:
    def __init__(self, path: str, line_length: int) -> None:
        self.path = path
        self.line_length = line_length
        self.sequences_written = 0

    def __enter__(self) -> _SequenceFileWriter:
        if self.path == '-':
            self.stream = sys.stdout
        else:
            self.stream = open(self.path, 'w', encoding='UTF-8')
        return self

    def __exit__(self, exc_type: type, exc_value: int, traceback: str) -> None:
        self.stream.close()


class FastaWriter:
    """Write fasta files."""

    def __init__(self, path: str, line_length: int = 80) -> None:
        self.writer = _SequenceFileWriter(path, line_length)

    def write_sequence(self, sequence: SequenceRecord) -> None:
        """Write single SeqRecord object to file."""
        assert hasattr(
            self.writer, 'stream'
        ), "Need to open file stream by running inside of 'with' block"
        if self.writer.line_length == -1:
            sequence_split = [sequence.sequence + '\n']
        else:
            sequence_split = [
                sequence.sequence[i : i + self.writer.line_length] + '\n'
                for i in range(0, len(sequence.sequence), self.writer.line_length)
            ]
        self.writer.stream.writelines([sequence.description + '\n'] + sequence_split)
        self.writer.sequences_written += 1

    def write_sequences(self, sequences: Iterable[SequenceRecord]) -> None:
        """Write multiple SeqRecord objects to file."""
        for sequence in sequences:
            self.write_sequence(sequence)

    def __enter__(self) -> FastaWriter:
        self.writer = self.writer.__enter__()
        return self

    def __exit__(self, exc_type: type, exc_value: int, traceback: str) -> None:
        self.writer.__exit__(exc_type, exc_value, traceback)


class FastqWriter:
    """Write fastq files"""

    def __init__(self, path: str, line_length: int = 80) -> None:
        self.writer = _SequenceFileWriter(path, line_length)

    def write_sequence(self, sequence: SequenceRecord) -> None:
        pass

    def write_sequences(self, sequences: Iterable[SequenceRecord]) -> None:
        pass

    def __enter__(self) -> FastqWriter:
        self.writer = self.writer.__enter__()
        return self

    def __exit__(self, exc_type: type, exc_value: int, traceback: str) -> None:
        self.writer.__exit__(exc_type, exc_value, traceback)
