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
