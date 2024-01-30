# unimog

> Elegant service objects for Python.

Composable business logic and uniform error handling for business logic actions.
A single action does one thing, and multiple actions can be organized in groups.
Groups and Actions can be arbitrarily nested and form complex DAGs (directed
acyclic graph).

Service objects are useful to represent complex business logic in an easy to
digest form.

## Usage

```bash
pip install unimog
```

### Action

```python
import gzip

from unimog import Action


class CompressText(Action):
    def perform(self):
        compressed_text = gzip.compress(self.context.input)
        return {"compressed_text": compressed_text}

result = CompressText()(input="Hello, World!")
result.is_success() # True
result.compressed_text # b'\x1f\x8b\x08\x00r\x92\xb7e…
```

### Organizer

```python
import gzip

from unimog import Action, Organizer


class CompressText(Action):
    def perform(self):
        compressed_text = gzip.compress(self.context.input)
        return {"compressed_text": compressed_text}

    
class DecompressText(Action):
    def perform(self):
        text = gzip.decompress(self.context.data)
        return {"text": text}

CompressAndDecompressText = Organizer(CompressText, DecompressText)

result = CompressAndDecompressText(input="Hello, World!")
result.is_success() # True
result.text # "Hello, World!"
```

## Contributing

### Tests

```bash
python -m pytest
```
