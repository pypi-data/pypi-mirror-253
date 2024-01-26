import tempfile
from pathlib import Path

from jinja2 import Environment

ERROR_IMAGE = b"iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9TpaItDnYQcchQdbEgKiJOWoUiVAi1QqsOJpd+QZOGpMXFUXAtOPixWHVwcdbVwVUQBD9AXF2cFF2kxP8lhRYxHhz34929x907QKiXmGZ1jAGaXjGT8ZiYzqyKgVcEEUIPZjAiM8uYk6QEPMfXPXx8vYvyLO9zf46QmrUY4BOJZ5lhVog3iKc2KwbnfeIwK8gq8TnxqEkXJH7kuuLyG+e8wwLPDJup5DxxmFjMt7HSxqxgasSTxBFV0ylfSLusct7irJWqrHlP/sJgVl9Z5jrNQcSxiCVIEKGgiiJKqCBKq06KhSTtxzz8A45fIpdCriIYORZQhgbZ8YP/we9urdzEuJsUjAGdL7b9MQQEdoFGzba/j227cQL4n4ErveUv14HpT9JrLS1yBPRuAxfXLU3ZAy53gP4nQzZlR/LTFHI54P2MvikD9N0C3Wtub819nD4AKeoqcQMcHALDecpe93h3V3tv/55p9vcDvfNyxR44FwEAAAAGYktHRAD/AP8A/6C9p5MAAAAJcEhZcwAALiMAAC4jAXilP3YAAAAHdElNRQfnDA0MACIsdQzGAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAsxJREFUeNrt3L8va2Ecx/HPuSFNJBYSk8UiwWCyGbpYSBg6SNgkGMwYhRjEYMHmL1CJNCkijc2g/QckkpL6FUsXShrq+d7hXLm5Ua0edUO930mX+vacJ3215zkMPDMz0ZfpF28BIAQIIAQIIAQIIAQIIAQIAQIIAQIIAQIIAQIIAUKAAEKAAEKAAEKAAEKAECCAECCAECCAECCAECAECCAECCD0LUCSSZnnFX/09r4919Ulm5qSDg4k50ofs9TsS5mMbH1dNjjoz09OymIx6eGh/Jrfc/xqZp/Z0ZE5ySybrWwunzdLpcw1Nprb3Q0+a2Z2eGiupcXc3p7Z7a1ZoWB2dWVuft7cyMjrtVV6/Cr3NUH+5FZWzPX1BZ+9vPQxEonX53x8NDc2Zm5mxsy5YMf/hL72HtLaKiUSUj4faNbicam7W144/Hq+vl7exIS0vCyl09VdS81u6ufnUk+PFAoFm93clIaGpLq64q9pb/fhjo+ru5avvocUfaytlb5uJ5P+XDxe/hpfbDaf95+LRt9e39OTvzdsbARbyydU9z8+6F42KzU1lf9wNDf/+0Q0Kq+//2Oznlf6pHd3H15LzV6yvGxWnpm8+3tpa0uam5MymWCzoZAUDks3N+UxWlo+tJba30MaGuRFIlIkIltclJ6fg80OD0uxmFQoFH/tyYn/5nd0VGctNft7yEunp/7zR0fBZi8u/D2i1G3v9PS7bnuLHv/H3fa2tUkLC7L19fKfzGKzra3ydnak0VHZ/r5/iXp+lq6vZUtLUi4nb3a2/D5T6Vq+5V2WZJbLlf8mpdP+z1KpymdfOjszt7pqbmDAXGenufFxc9vbf8//3m/1W8evYh7/Jpa/9hIggBAggBAggBAggBAgBAggBAggBAggBAggBAgBAggBAggBAggBAggBQoAAQoAAQoAAQoAAQoAQIIAQIIAQIIAQID+v3y6u/TaG724dAAAAAElFTkSuQmCC"


class RenderContext:
    def __init__(self, output=Path | str | None):
        if output is None:
            output = tempfile.mkdtemp(prefix="unireport_")

        self.output_dir: Path = Path(output)
        self.error_image_base64: bytes = ERROR_IMAGE

    def get_images_dir(self) -> Path:
        src_dir = self.output_dir / "src"
        if not src_dir.exists():
            src_dir.mkdir()

        return src_dir


class Plugin:
    def __init__(self):
        self.context: RenderContext | None = None

    def setup(self, _: Environment):
        pass

    def set_context(self, context: RenderContext):
        self.context = context
