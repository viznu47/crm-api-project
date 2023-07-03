from transformers import pipeline

# Initialize the sentiment analysis pipeline
sent_pipeline = pipeline("sentiment-analysis")

# Get the maximum sequence length for each model
model_sequence_lengths = {
    model_name: sent_pipeline.model.config.max_position_embeddings
    for model_name in sent_pipeline.model_names
}

# Find the model with the highest sequence length
max_sequence_length_model = max(model_sequence_lengths, key=model_sequence_lengths.get)

print("Model with the highest sequence length:", max_sequence_length_model)
print("Maximum sequence length:", model_sequence_lengths[max_sequence_length_model])
