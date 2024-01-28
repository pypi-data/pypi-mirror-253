
import gradio as gr
from app import demo as app
import os

_docs = {'HighlightedTextbox': {'description': 'Creates a textarea for user to enter string input or display string output where some\nelements are highlighted.\n    (1) "text" whose value is the complete text, and\n    (2) "highlights", which is a list of dictionaries, each of which have the keys:\n        "highlight_type" (consisting of the highlight label),\n        "start" (the character index where the label starts), and\n        "end" (the character index where the label ends).\n    Highlights should not overlap.', 'members': {'__init__': {'value': {'type': 'str | Callable | None', 'default': '""', 'description': 'default text to provide in textbox. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'color_map': {'type': 'dict[str, str] | None', 'default': 'None', 'description': 'dictionary mapping labels to colors.'}, 'show_legend': {'type': 'bool', 'default': 'False', 'description': 'if True, will display legend.'}, 'show_legend_label': {'type': 'bool', 'default': 'False', 'description': 'if True, will display legend label.'}, 'legend_label': {'type': 'str', 'default': '""', 'description': 'label to display above legend.'}, 'combine_adjacent': {'type': 'bool', 'default': 'False', 'description': 'if True, will combine adjacent spans with the same label.'}, 'adjacent_separator': {'type': 'str', 'default': '""', 'description': 'separator to use when combining adjacent spans.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'component name in interface.'}, 'info': {'type': 'str | None', 'default': 'None', 'description': None}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'autofocus': {'type': 'bool', 'default': 'False', 'description': None}, 'autoscroll': {'type': 'bool', 'default': 'True', 'description': 'If True, will automatically scroll to the bottom of the textbox when the value changes, unless the user scrolls up. If False, will not scroll to the bottom of the textbox when the value changes.'}, 'interactive': {'type': 'bool', 'default': 'True', 'description': 'if True, will be rendered as an editable textbox; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'show_copy_button': {'type': 'bool', 'default': 'False', 'description': 'If True, includes a copy button to copy the text in the textbox. Only applies if show_label is True.'}}, 'postprocess': {'y': {'type': 'list[tuple[str, str | None]] | dict | None', 'description': 'List of (word, category) tuples, or a dictionary of two keys: "text", and "highlights", which itself is'}, 'value': {'type': 'list[tuple[str, str | None]] | dict | None', 'description': 'List of (word, category) tuples, or a dictionary of two keys: "text", and "highlights", which itself is'}}, 'preprocess': {'return': {'type': 'dict', 'description': None}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the HighlightedTextbox changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'input': {'type': None, 'default': None, 'description': 'This listener is triggered when the user changes the value of the HighlightedTextbox.'}, 'select': {'type': None, 'default': None, 'description': 'Event listener for when the user selects or deselects the HighlightedTextbox. Uses event data gradio.SelectData to carry `value` referring to the label of the HighlightedTextbox, and `selected` to refer to state of the HighlightedTextbox. See EventData documentation on how to use this event data'}, 'submit': {'type': None, 'default': None, 'description': 'This listener is triggered when the user presses the Enter key while the HighlightedTextbox is focused.'}, 'focus': {'type': None, 'default': None, 'description': 'This listener is triggered when the HighlightedTextbox is focused.'}, 'blur': {'type': None, 'default': None, 'description': 'This listener is triggered when the HighlightedTextbox is unfocused/blurred.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'HighlightedTextbox': []}}}
    
abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_highlightedtextbox`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_highlightedtextbox/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_highlightedtextbox"></a>  <a href="https://huggingface.co/spaces/gsarti/gradio_highlightedtextbox/discussions" target="_blank"><img alt="Static Badge" src="https://img.shields.io/badge/%F0%9F%A4%97%20Discuss-%23097EFF?style=flat&logoColor=black"></a>
</div>

Editable Gradio textarea supporting highlighting
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_highlightedtextbox
```

## Usage

```python
import gradio as gr
from gradio_highlightedtextbox import HighlightedTextbox


def convert_tagged_text_to_highlighted_text(
    tagged_text: str,
    tag_id: str | list[str],
    tag_open: str | list[str],
    tag_close: str | list[str],
) -> list[tuple[str, str | None]]:
    return HighlightedTextbox.tagged_text_to_tuples(
        tagged_text, tag_id, tag_open, tag_close
    )


def convert_highlighted_text_to_tagged_text(
    highlighted_text: dict[str, str | list[tuple[str, str | None]]],
    tag_id: str | list[str],
    tag_open: str | list[str],
    tag_close: str | list[str],
) -> str:
    return HighlightedTextbox.tuples_to_tagged_text(
        highlighted_text["data"], tag_id, tag_open, tag_close
    )


initial_text = "It is not something to be ashamed of: it is no different from the <d>personal fears</d> and <tm>dislikes</tm> of other things that <t>manny peopl</t> have."

with gr.Blocks() as demo:
    gr.Markdown("### Parameters to control the highlighted textbox:")
    with gr.Row():
        tag_id = gr.Dropdown(
            choices=["Typo", "Terminology", "Disfluency"],
            value=["Typo", "Terminology", "Disfluency"],
            multiselect=True,
            allow_custom_value=True,
            label="Tag ID",
            show_label=True,
            info="Insert one or more tag IDs to use in the highlighted textbox.",
        )
        tag_open = gr.Dropdown(
            choices=["<t>", "<tm>", "<d>"],
            value=["<t>", "<tm>", "<d>"],
            multiselect=True,
            allow_custom_value=True,
            label="Tag open",
            show_label=True,
            info="Insert one or more tags to mark the beginning of a highlighted section.",
        )
        tag_close = gr.Dropdown(
            choices=["</t>", "</tm>", "</d>"],
            value=["</t>", "</tm>", "</d>"],
            multiselect=True,
            allow_custom_value=True,
            label="Tag close",
            show_label=True,
            info="Insert one or more tags to mark the end of a highlighted section.",
        )
    gr.Markdown("### Example tagged to highlight:")
    with gr.Row():
        tagged_t2h = gr.Textbox(
            initial_text,
            interactive=True,
            label="Tagged Input",
            show_label=True,
            info="Tagged text using the format above to mark spans that will be highlighted.",
        )
        high_t2h = HighlightedTextbox(
            convert_tagged_text_to_highlighted_text(
                tagged_t2h.value, tag_id.value, tag_open.value, tag_close.value
            ),
            interactive=False,
            label="Highlighted Output",
            info="Highlighted textbox intialized from the tagged input.",
            show_legend=True,
            show_label=True,
            legend_label="Legend:",
            show_legend_label=True,
        )
    gr.Markdown("### Example highlight to tagged:")
    with gr.Row():
        high_h2t = HighlightedTextbox(
            convert_tagged_text_to_highlighted_text(
                initial_text, tag_id.value, tag_open.value, tag_close.value
            ),
            interactive=True,
            label="Highlighted Input",
            info="Highlighted textbox using the format above to mark spans that will be highlighted.",
            show_legend=True,
            show_label=True,
            legend_label="Legend:",
            show_legend_label=True,
        )
        tagged_h2t = gr.Textbox(
            initial_text,
            interactive=False,
            label="Tagged Output",
            info="Tagged text intialized from the highlighted textbox.",
            show_label=True,
        )

    # Functions

    tagged_t2h.input(
        fn=convert_tagged_text_to_highlighted_text,
        inputs=[tagged_t2h, tag_id, tag_open, tag_close],
        outputs=high_t2h,
    )
    high_h2t.input(
        fn=convert_highlighted_text_to_tagged_text,
        inputs=[high_h2t, tag_id, tag_open, tag_close],
        outputs=tagged_h2t,
    )

if __name__ == "__main__":
    demo.launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `HighlightedTextbox`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["HighlightedTextbox"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["HighlightedTextbox"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function. 
- When used as an output, the component only impacts the return signature of the user function. 

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Should return, list of (word, category) tuples, or a dictionary of two keys: "text", and "highlights", which itself is.

 ```python
def predict(
    value: dict
) -> list[tuple[str, str | None]] | dict | None:
    return value
```
""", elem_classes=["md-custom", "HighlightedTextbox-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          HighlightedTextbox: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
        
        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
