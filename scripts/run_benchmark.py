import os
import re
import json
from openai import OpenAI

# --- CONFIGURAÇÃO ---
# 1. Instale a biblioteca da OpenAI: pip install openai
# 2. Obtenha uma chave de API de um provedor (OpenAI, Groq, etc.)
# 3. Insira sua chave de API abaixo.
API_KEY = "SUA_CHAVE_API_AQUI"

# 4. (Opcional) Se usar um provedor diferente da OpenAI, ajuste a URL base.
# Exemplo para Groq: BASE_URL = "https://api.groq.com/openai/v1"
BASE_URL = "https://api.openai.com/v1"

# 5. Escolha o modelo que deseja usar.
# Ex. para OpenAI: "gpt-4o", "gpt-3.5-turbo"
# Ex. para Groq: "llama3-70b-8192", "gemma-7b-it"
MODEL_NAME = "gpt-3.5-turbo"

# 6. MODO_SIMULADO: Se True, não fará chamadas de API reais.
#    Útil para testar o script sem gastar créditos ou sem ter uma chave.
#    Para executar de verdade, mude para False.
MODO_SIMULADO = True

# --- CONSTANTES DO PROJETO ---
BENCHMARK_DIR = 'benchmark'
PROMPT_FILE = 'prompts.md'
OUTPUT_FILE_SUFFIX = '_gptapi.md'

def parse_prompts(file_path):
    """
    Extrai os três tipos de prompts (Genérico, JSON, KERNEL) de um arquivo .md.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"  -> Aviso: Arquivo de prompts não encontrado em {file_path}")
        return None

    prompts = {}

    # Regex para capturar cada seção de prompt
    # ## 1. Prompt Genérico\n\n(CONTEÚDO)\n\n---
 generico_match = re.search(r'## 1. Prompt Genérico\n\n(.*?)\n\n---', content, re.DOTALL)
    if generico_match:
        prompts['generico'] = generico_match.group(1).strip()

    # ## 2. Prompt Estruturado (JSON)\n\n```json\n(CONTEÚDO)\n```
    json_match = re.search(r'## 2. Prompt Estruturado \(JSON\)\n\n```json\n(.*?)\n```', content, re.DOTALL)
    if json_match:
        # Para o prompt JSON, enviamos o objeto inteiro como string
        prompts['json'] = f"```json\n{json_match.group(1).strip()}\n```"

    # ## 3. Prompt Estruturado (KERNEL)\n\n(CONTEÚDO ATÉ O FIM)
    kernel_match = re.search(r'## 3. Prompt Estruturado \(KERNEL\)\n\n(.*?)$', content, re.DOTALL)
    if kernel_match:
        prompts['kernel'] = kernel_match.group(1).strip()

    return prompts

def call_model_api(prompt_text):
    """
    Chama a API do modelo de linguagem ou retorna uma resposta simulada.
    """
    if MODO_SIMULADO:
        print(f"    -> [MODO SIMULADO] Enviando prompt...")
        return f"[RESPOSTA SIMULADA DA API PARA O PROMPT ACIMA]"

    if not API_KEY or API_KEY == "SUA_CHAVE_API_AQUI":
        print("  -> Erro: A variável API_KEY não foi definida. Preencha-a para usar o modo real.")
        return "[ERRO: CHAVE DE API NÃO CONFIGURADA]"

    try:
        print(f"    -> Chamando API com o modelo {MODEL_NAME}...")
        client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Você é um assistente prestativo e especialista em seguir instruções."},
                {"role": "user", "content": prompt_text},
            ]
        )
        print("    -> Resposta recebida.")
        return response.choices[0].message.content
    except Exception as e:
        print(f"  -> Erro ao chamar a API: {e}")
        return f"[ERRO AO CHAMAR A API: {e}]"

def main():
    """
    Função principal que orquestra o processo de benchmark.
    """
    print("Iniciando script de benchmark de API...")

    if not os.path.isdir(BENCHMARK_DIR):
        print(f"Erro: Diretório '{BENCHMARK_DIR}' não encontrado.")
        return

    # Percorre todos os subdiretórios na pasta benchmark
    for dir_name in sorted(os.listdir(BENCHMARK_DIR)):
        assistente_dir = os.path.join(BENCHMARK_DIR, dir_name)
        
        if os.path.isdir(assistente_dir):
            print(f"\nProcessando assistente: {dir_name}")
            
            prompt_file_path = os.path.join(assistente_dir, PROMPT_FILE)
            
            prompts = parse_prompts(prompt_file_path)
            if not prompts:
                continue

            final_output_content = f"# RESULTADO DO BENCHMARK (API: {MODEL_NAME})\n\n"
            final_output_content += "Este arquivo documenta os resultados gerados via API para cada um dos três tipos de prompt.\n\n"

            # 1. Processa Prompt Genérico
            print("  - Processando Prompt Genérico...")
            prompt_generico = prompts.get('generico', '[PROMPT GENÉRICO NÃO ENCONTRADO]')
            resposta_generica = call_model_api(prompt_generico)
            final_output_content += f"---\n\n## 1. Resposta ao Prompt Genérico\n\n**Prompt:**\n`{prompt_generico}`\n\n**Resultado da API:**\n{resposta_generica}\n\n"

            # 2. Processa Prompt JSON
            print("  - Processando Prompt Estruturado (JSON)...")
            prompt_json = prompts.get('json', '[PROMPT JSON NÃO ENCONTRADO]')
            resposta_json = call_model_api(prompt_json)
            final_output_content += f"---\n\n## 2. Resposta ao Prompt Estruturado (JSON)\n\n**Prompt:**\n{prompt_json}\n\n**Resultado da API:**\n{resposta_json}\n\n"

            # 3. Processa Prompt KERNEL
            print("  - Processando Prompt Estruturado (KERNEL)...")
            prompt_kernel = prompts.get('kernel', '[PROMPT KERNEL NÃO ENCONTRADO]')
            resposta_kernel = call_model_api(prompt_kernel)
            final_output_content += f"---\n\n## 3. Resposta ao Prompt Estruturado (KERNEL)\n\n**Prompt:**\n```\n{prompt_kernel}\n```\n\n**Resultado da API:**\n{resposta_kernel}\n\n"

            # Salva o arquivo de resultado
            output_file_name = f"resultado{OUTPUT_FILE_SUFFIX}"
            output_file_path = os.path.join(assistente_dir, output_file_name)
            
            try:
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(final_output_content)
                print(f"  -> Sucesso! Arquivo salvo em: {output_file_path}")
            except Exception as e:
                print(f"  -> Erro ao salvar o arquivo {output_file_path}: {e}")

    print("\nScript de benchmark concluído!")
    if MODO_SIMULADO:
        print("\nLembrete: O script rodou em MODO SIMULADO. Para resultados reais, edite o script, insira sua chave de API e mude MODO_SIMULADO para False.")

if __name__ == "__main__":
    main()
