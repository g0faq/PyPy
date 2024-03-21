import docx2txt
import openai

# Set your OpenAI API key
client = openai.OpenAI()


def parse_tasks(docx_path):
    text = docx2txt.process(docx_path)
    tasks = [task.strip() for task in text.split('\n') if task.strip()]
    return tasks

# Example usage:
def generate_responses(tasks):
    responses = []

    for task in tasks:
        prompt = f"Task: {task}\nResponse:"
        response = client.completions.create(
            model="davinci-002",
            prompt=prompt,
            max_tokens=150)
        response_text = response['choices'][0]['text'].strip()
        responses.append(response_text)

    return responses


docx_path = "Задачи_24.docx"
parsed_tasks = parse_tasks(docx_path)

responses = generate_responses(parsed_tasks)

for task, response in zip(parsed_tasks, responses):
    print(f"Task: {task}")
    print(f"Response: {response}\n")







