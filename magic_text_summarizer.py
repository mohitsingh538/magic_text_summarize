from summarizer import Summarizer, TransformerSummarizer


class Summarize_Paragraph:

    def __init__(self, model_name: str):
        self.model_name = model_name

    def this_paragraph(self, paragraph: str) -> str:
        #   GPT-2
        if self.model_name == "GPT-2":
            try:
                GPT2_model = TransformerSummarizer(transformer_type="GPT2", transformer_model_key="gpt2-medium")
                full = ''.join(GPT2_model(paragraph, min_length=5))
                return full

            except Exception as e:
                raise Exception(e)

        #   BERT
        elif self.model_name == 'BERT':
            try:
                bert_model = Summarizer()
                bert_summary = ''.join(bert_model(paragraph, min_length=10))
                return bert_summary

            except Exception as e:
                raise Exception(e)

        #   XLNet
        elif self.model_name == 'XLNet':
            try:
                model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")
                full = ''.join(model(paragraph, min_length=10))
                return full

            except Exception as e:
                raise Exception(e)
