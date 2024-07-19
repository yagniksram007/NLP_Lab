# 9. Implement a machine translator for 10 words using encoder-decoder model
# for any two languages.

import os
import sys
import transformers
import tensorflow as tf
from datasets import load_dataset
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, AdamWeightDecay

# Model checkpoint for English to Hindi translation
model_checkpoint = "Helsinki-NLP/opus-mt-en-hi"

# Load dataset
raw_datasets = load_dataset("cfilt/iitb-english-hindi")
print(raw_datasets)
print(raw_datasets['train'][1])

# Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
print(tokenizer("Hello, this is a sentence!"))

max_input_length = 128
max_target_length = 128
source_lang = "en"
target_lang = "hi"

def preprocess_function(examples):
    inputs = [ex[source_lang] for ex in examples["translation"]]
    targets = [ex[target_lang] for ex in examples["translation"]]
    model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True)
    # Setup the tokenizer for targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(targets, max_length=max_target_length, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Preprocess the dataset
preprocess_function(raw_datasets["train"][:2])
tokenized_datasets = raw_datasets.map(preprocess_function, batched=True)

# Initialize the model
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)

batch_size = 16
learning_rate = 2e-5
weight_decay = 0.01
num_train_epochs = 1

data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, return_tensors="tf")
generation_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model, return_tensors="tf", pad_to_multiple_of=128)

train_dataset = model.prepare_tf_dataset(
    tokenized_datasets["test"],
    batch_size=batch_size,
    shuffle=True,
    collate_fn=data_collator,
)

validation_dataset = model.prepare_tf_dataset(
    tokenized_datasets["validation"],
    batch_size=batch_size,
    shuffle=False,
    collate_fn=data_collator,
)

generation_dataset = model.prepare_tf_dataset(
    tokenized_datasets["validation"],
    batch_size=8,
    shuffle=False,
    collate_fn=generation_data_collator,
)

optimizer = AdamWeightDecay(learning_rate=learning_rate, weight_decay_rate=weight_decay)
model.compile(optimizer=optimizer)
model.fit(train_dataset, validation_data=validation_dataset, epochs=num_train_epochs)

# Save the model
model.save_pretrained("tf_model/")

# Load the saved model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = TFAutoModelForSeq2SeqLM.from_pretrained("tf_model/")

# Translate a sample input text
input_text = "hello India"
tokenized = tokenizer([input_text], return_tensors='np')
out = model.generate(**tokenized, max_length=128)
print(out)

with tokenizer.as_target_tokenizer():
    print(tokenizer.decode(out[0], skip_special_tokens=True))

# Output:
