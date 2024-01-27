
# `gradio_highlightedtextbox`
<a href="https://pypi.org/project/gradio_highlightedtextbox/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_highlightedtextbox"></a>  <a href="https://huggingface.co/spaces/gsarti/gradio_highlightedtextbox/discussions" target="_blank"><img alt="Static Badge" src="https://img.shields.io/badge/%F0%9F%A4%97%20Discuss-%23097EFF?style=flat&logoColor=black"></a>

Editable Gradio textarea supporting highlighting

## Installation
    
```bash 
pip install gradio_highlightedtextbox
```

## Usage

```python
import gradio as gr
from gradio_highlightedtextbox import HighlightedTextbox


def convert_tagged_text_to_highlighted_text(
    tagged_text: str, tag_id: str, tag_open: str, tag_close: str
) -> list[tuple[str, str | None]]:
    return HighlightedTextbox.tagged_text_to_tuples(
        tagged_text, tag_id, tag_open, tag_close
    )


def convert_highlighted_text_to_tagged_text(
    highlighted_text: dict[str, str | list[tuple[str, str | None]]],
    tag_id: str,
    tag_open: str,
    tag_close: str,
) -> str:
    return HighlightedTextbox.tuples_to_tagged_text(
        highlighted_text["data"], tag_id, tag_open, tag_close
    )


initial_text = "It is not something to be ashamed of: it is no different from the <h>personal fears</h> and <h>dislikes</h> of other things that <h>very many people</h> have."

with gr.Blocks() as demo:
    tag_id = gr.Textbox(
        "Potential issue",
        label="Tag ID",
        show_label=True,
        info="Insert a tag ID to use in the highlighted textbox.",
    )
    tag_open = gr.Textbox(
        "<h>",
        label="Tag open",
        show_label=True,
        info="Insert a tag to mark the beginning of a highlighted section.",
    )
    tag_close = gr.Textbox(
        "</h>",
        label="Tag close",
        show_label=True,
        info="Insert a tag to mark the end of a highlighted section.",
    )
    with gr.Row():
        tagged_t2h = gr.Textbox(
            initial_text,
            interactive=True,
            label="Input",
            show_label=True,
            info="Insert a text with <h>...</h> tags to mark spans that will be highlighted.",
        )
        high_t2h = HighlightedTextbox(
            convert_tagged_text_to_highlighted_text(
                tagged_t2h.value, tag_id.value, tag_open.value, tag_close.value
            ),
            interactive=True,
            label="Output",
            info="Highlighted textbox.",
            show_legend=True,
            show_label=True,
            legend_label="Legend:",
            show_legend_label=True,
        )
    with gr.Row():
        high_h2t = HighlightedTextbox(
            convert_tagged_text_to_highlighted_text(
                tagged_t2h.value, tag_id.value, tag_open.value, tag_close.value
            ),
            interactive=True,
            label="Input",
            info="The following text will be marked by spans according to its highlights.",
            show_legend=True,
            show_label=True,
            legend_label="Legend:",
            show_legend_label=True,
        )
        tagged_h2t = gr.Textbox(
            initial_text,
            interactive=True,
            label="Output",
            show_label=True,
        )

    # Functions

    tagged_t2h.change(
        fn=convert_tagged_text_to_highlighted_text,
        inputs=[tagged_t2h, tag_id, tag_open, tag_close],
        outputs=high_t2h,
    )
    high_t2h.change(
        fn=lambda x: x["data"],
        inputs=high_t2h,
        outputs=high_h2t,
    )
    high_h2t.change(
        fn=convert_highlighted_text_to_tagged_text,
        inputs=[high_h2t, tag_id, tag_open, tag_close],
        outputs=tagged_h2t,
    )


demo.launch()

```

## `HighlightedTextbox`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
str | Callable | None
```

</td>
<td align="left"><code>""</code></td>
<td align="left">default text to provide in textbox. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>color_map</code></td>
<td align="left" style="width: 25%;">

```python
dict[str, str] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">dictionary mapping labels to colors.</td>
</tr>

<tr>
<td align="left"><code>show_legend</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">if True, will display legend.</td>
</tr>

<tr>
<td align="left"><code>show_legend_label</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">if True, will display legend label.</td>
</tr>

<tr>
<td align="left"><code>legend_label</code></td>
<td align="left" style="width: 25%;">

```python
str
```

</td>
<td align="left"><code>""</code></td>
<td align="left">label to display above legend.</td>
</tr>

<tr>
<td align="left"><code>combine_adjacent</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">if True, will combine adjacent spans with the same label.</td>
</tr>

<tr>
<td align="left"><code>adjacent_separator</code></td>
<td align="left" style="width: 25%;">

```python
str
```

</td>
<td align="left"><code>""</code></td>
<td align="left">separator to use when combining adjacent spans.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">component name in interface.</td>
</tr>

<tr>
<td align="left"><code>info</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will place the component in a container - providing some extra padding around the border.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>autofocus</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>autoscroll</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If True, will automatically scroll to the bottom of the textbox when the value changes, unless the user scrolls up. If False, will not scroll to the bottom of the textbox when the value changes.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">if True, will be rendered as an editable textbox; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>show_copy_button</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, includes a copy button to copy the text in the textbox. Only applies if show_label is True.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the HighlightedTextbox changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `input` | This listener is triggered when the user changes the value of the HighlightedTextbox. |
| `select` | Event listener for when the user selects or deselects the HighlightedTextbox. Uses event data gradio.SelectData to carry `value` referring to the label of the HighlightedTextbox, and `selected` to refer to state of the HighlightedTextbox. See EventData documentation on how to use this event data |
| `submit` | This listener is triggered when the user presses the Enter key while the HighlightedTextbox is focused. |
| `focus` | This listener is triggered when the HighlightedTextbox is focused. |
| `blur` | This listener is triggered when the HighlightedTextbox is unfocused/blurred. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function. 
- When used as an output, the component only impacts the return signature of the user function. 

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Should return, list of (word, category) tuples, or a dictionary of two keys: "text", and "highlights", which itself is.

 ```python
 def predict(
     value: dict
 ) -> list[tuple[str, str | None]] | dict | None:
     return value
 ```
 
