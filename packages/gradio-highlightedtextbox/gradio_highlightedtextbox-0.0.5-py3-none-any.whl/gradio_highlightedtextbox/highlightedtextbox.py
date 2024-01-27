from __future__ import annotations

from typing import Any, Callable

from gradio.components.base import FormComponent
from gradio.data_classes import GradioRootModel
from gradio.events import Events


class HighlightedTextData(GradioRootModel):
    root: list[tuple[str, str | None]]


class HighlightedTextbox(FormComponent):
    """
    Creates a textarea for user to enter string input or display string output where some
    elements are highlighted.
    Preprocessing: passes a list of tuples as a {List[Tuple[str, float | str | None]]]} into the function. If no labels are provided, the text will be displayed as a single span.
    Postprocessing: expects a {List[Tuple[str, float | str]]]} consisting of spans of text and their associated labels, or a {Dict} with two keys:
        (1) "text" whose value is the complete text, and
        (2) "highlights", which is a list of dictionaries, each of which have the keys:
            "highlight_type" (consisting of the highlight label),
            "start" (the character index where the label starts), and
            "end" (the character index where the label ends).
        Highlights should not overlap.
    """

    EVENTS = [
        Events.change,
        Events.input,
        Events.select,
        Events.submit,
        Events.focus,
        Events.blur,
    ]
    data_model = HighlightedTextData

    def __init__(
        self,
        value: str | Callable | None = "",
        *,
        color_map: dict[str, str] | None = None,
        show_legend: bool = False,
        show_legend_label: bool = False,
        legend_label: str = "",
        combine_adjacent: bool = False,
        adjacent_separator: str = "",
        label: str | None = None,
        info: str | None = None,
        every: float | None = None,
        show_label: bool | None = None,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        visible: bool = True,
        elem_id: str | None = None,
        autofocus: bool = False,
        autoscroll: bool = True,
        interactive: bool = True,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        show_copy_button: bool = False,
    ):
        """
        Parameters:
            value: default text to provide in textbox. If callable, the function will be called whenever the app loads to set the initial value of the component.
            lines: number of lines to display in textbox.
            max_lines: maximum number of lines to display in textbox.
            color_map: dictionary mapping labels to colors.
            show_legend: if True, will display legend.
            show_legend_label: if True, will display legend label.
            legend_label: label to display above legend.
            combine_adjacent: if True, will combine adjacent spans with the same label.
            adjacent_separator: separator to use when combining adjacent spans.
            placeholder: placeholder hint to provide behind textbox.
            label: component name in interface.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            interactive: if True, will be rendered as an editable textbox; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.
            visible: If False, component will be hidden.
            rtl: If True and `type` is "text", sets the direction of the text to right-to-left (cursor appears on the left of the text). Default is False, which renders cursor on the right.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
            rtl: If True and `type` is "text", sets the direction of the text to right-to-left (cursor appears on the left of the text). Default is False, which renders cursor on the right.
            show_copy_button: If True, includes a copy button to copy the text in the textbox. Only applies if show_label is True.
            autoscroll: If True, will automatically scroll to the bottom of the textbox when the value changes, unless the user scrolls up. If False, will not scroll to the bottom of the textbox when the value changes.
        """
        self.color_map = color_map
        self.show_legend = show_legend
        self.show_legend_label = show_legend_label
        self.legend_label = legend_label
        self.combine_adjacent = combine_adjacent
        self.adjacent_separator = adjacent_separator
        self.show_copy_button = show_copy_button
        self.autofocus = autofocus
        self.autoscroll = autoscroll
        super().__init__(
            label=label,
            info=info,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            render=render,
            every=every,
        )

    def preprocess(self, payload: HighlightedTextData) -> dict:
        return {"id": self.elem_id, "data": payload.root}

    def postprocess(
        self, y: list[tuple[str, str | None]] | dict | None
    ) -> list[tuple[str, str | None]] | None:
        """
        Parameters:
            y: List of (word, category) tuples, or a dictionary of two keys: "text", and "highlights", which itself is
                a list of dictionaries, each of which have the keys: "highlight_type", "start", and "end"
        Returns:
            List of (word, category) tuples
        """
        if y is None:
            return None
        if isinstance(y, dict):
            try:
                text = y["text"]
                highlights = y["highlights"]
            except KeyError as ke:
                raise ValueError(
                    "Expected a dictionary with keys 'text' and 'highlights' "
                    "for the value of the HighlightedText component."
                ) from ke
            if len(highlights) == 0:
                y = [(text, None)]
            else:
                list_format = []
                index = 0
                entities = sorted(highlights, key=lambda x: x["start"])
                for entity in entities:
                    list_format.append((text[index : entity["start"]], None))
                    highlight_type = entity.get("highlight_type")
                    list_format.append(
                        (text[entity["start"] : entity["end"]], highlight_type)
                    )
                    index = entity["end"]
                list_format.append((text[index:], None))
                y = list_format
        if self.combine_adjacent:
            output = []
            running_text, running_category = None, None
            for text, category in y:
                if running_text is None:
                    running_text = text
                    running_category = category
                elif category == running_category:
                    running_text += self.adjacent_separator + text
                elif not text:
                    # Skip fully empty item, these get added in processing
                    # of dictionaries.
                    pass
                else:
                    output.append((running_text, running_category))
                    running_text = text
                    running_category = category
            if running_text is not None:
                output.append((running_text, running_category))
            return output
        else:
            return y

    def example_inputs(self) -> Any:
        return [("Hello", None), ("world", "highlight")]

    @classmethod
    def tagged_text_to_tuples(
        cls, text: str, tag_id: str, tag_open: str = "<h>", tag_close: str = "</h>"
    ) -> list[tuple[str, str | None]]:
        """Parse a text containing tags into a list of tuples in the format accepted by HighlightedTextbox.

        E.g. Hello <h>world</h>! -> [("Hello", None), ("world", <TAG_ID>), ("!", None)]

        Args:
            text (`str`):
                Text containing tags that needs to be parsed.
            tag_id (`str`):
                Label to use for the second element of the tuple.
            tag_open (`str`, *optional*, defaults to "<h>"):
                Tag used to mark the beginning of a highlighted section.
            tag_close (`str`, *optional*, defaults to "</h>"):
                Tag used to mark the end of a highlighted section.

        Raises:
            `ValueError`: Number of open tags does not match number of closed tags.

        Returns:
            `list[tuple[str, str | None]]`: List of tuples in the format accepted by HighlightedTextbox.
        """
        # Check that the text is well-formed (i.e. no nested or empty tags)
        num_tags = text.count(tag_open)
        if num_tags != text.count(tag_close):
            raise ValueError(
                f"Number of open tags ({tag_open}) does not match number of closed tags ({tag_close})."
            )
        elif num_tags == 0:
            return [(text, None)]
        elif num_tags > 0:
            out = []
            pre_tag_text = text[: text.index(tag_open)]
            if pre_tag_text:
                out += [(pre_tag_text.strip(), None)]

            tag_text = text[
                text.index(tag_open) + len(tag_open) : text.index(tag_close)
            ]
            out += [(tag_text.strip(), tag_id)]
            if num_tags > 1:
                remaining_text = text[text.index(tag_close) + len(tag_close) :]
                out += cls.tagged_text_to_tuples(
                    remaining_text,
                    tag_id=tag_id,
                    tag_open=tag_open,
                    tag_close=tag_close,
                )
            else:
                post_tag_text = text[text.index(tag_close) + len(tag_close) :]
                if post_tag_text:
                    out += [(post_tag_text, None)]
        return out

    @staticmethod
    def tuples_to_tagged_text(
        tuples: list[tuple[str, str | None]],
        tag_ids: str | list[str] = [],
        tag_open: str = "<h>",
        tag_close: str = "</h>",
    ) -> str:
        """Convert a list of tuples in the format accepted by HighlightedTextbox into a text containing tags.

        E.g. [("Hello", None), ("world", <TAG_ID>), ("!", None)] -> Hello <h>world</h>!

        Args:
            tuples (`list[tuple[str, str | None]]`):
                List of tuples in the format accepted by HighlightedTextbox.
            tag_ids (`str` | `list[str]`):
                Label(s) to select for the second element of the tuple. All other labels will be ignored
                (i.e. replaced with None)
            tag_open (`str`, *optional*, defaults to "<h>"):
                Tag used to mark the beginning of a highlighted section.
            tag_close (`str`, *optional*, defaults to "</h>"):
                Tag used to mark the end of a highlighted section.

        Returns:
            `str`: Text containing tags.
        """
        if isinstance(tag_ids, str):
            tag_ids = [tag_ids]
        out = ""
        for text, tag_id in tuples:
            space_or_not = (
                " "
                if text not in [".", "!", "?", ",", ":", ")", "]", ";", "}", """'"""]
                else ""
            )
            if tag_id in tag_ids:
                out += f"{space_or_not}{tag_open}{text.strip()}{tag_close}"
            else:
                out += f"{space_or_not}{text.strip()} "
        return out.strip()
