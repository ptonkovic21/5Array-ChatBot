from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import torch

model_name_ai = "deepseek-ai/deepseek-llm-7b-chat"
model_name_embedding = "sentence-transformers/all-mpnet-base-v2"
dataset = "vectorised_dataset"

embeddings = HuggingFaceEmbeddings(model_name=model_name_embedding)
tokenizer = AutoTokenizer.from_pretrained(model_name_ai)

data = FAISS.load_local(
    dataset, 
    embeddings,
    allow_dangerous_deserialization=True)

model = AutoModelForCausalLM.from_pretrained(
    model_name_ai,
    torch_dtype=torch.float16,
    device_map="auto",
    
    # Koristiti ovo u slučaju da imate slabo računalo 
    # Podesite po vašim mogućnostima

    max_memory={0: "2500MiB", "cpu": "10GB"},
    offload_folder="./offload"
)

model.generation_config = GenerationConfig.from_pretrained(model_name_ai)

model.generation_config.pad_token_id = model.generation_config.eos_token_id

def ask(question: str):
    retriever = data.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(question)
    context = "\n\n".join([doc.page_content for doc in docs])

    messages = [
        {"role": "system", 
        "content": "You are a helpful assistant. Study the provided context carefully and answer the provided question. Be cheerful and friendly. Read the context multiple times and only give the correct answer. If you are not sure about something don't say it. Do not qoute directly what is written! Think about what the user wrote and take into account the format of the question, for example how dates are written. Answer more openly!"},
        {"role": "user", 
        "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]

    input_tensor = tokenizer.apply_chat_template(
        messages, 
        add_generation_prompt=True, 
        return_tensors="pt")
    
    outputs = model.generate(
        input_tensor.to(model.device), 
        max_new_tokens=100)
    
    result = tokenizer.decode(
        outputs[0][input_tensor.shape[1]:], 
        skip_special_tokens=True)
    
    return result.strip()
