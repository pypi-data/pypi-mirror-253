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
