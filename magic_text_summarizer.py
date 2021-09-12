from summarizer import Summarizer, TransformerSummarizer

class Summarize_Paragraph():

    def this_paragraph(model_name, paragraph): 
    #   GPT-2
        if model_name == "GPT-2":   
            GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
            full = ''.join(GPT2_model(paragraph, min_length=5))
            return full

    #   BERT
        elif model_name == 'BERT':
            bert_model = Summarizer()
            bert_summary = ''.join(bert_model(paragraph, min_length=10))
            return bert_summary


    #   XLNet
        elif model_name == 'XLNet':
            model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")
            full = ''.join(model(paragraph, min_length=10))
            return full


