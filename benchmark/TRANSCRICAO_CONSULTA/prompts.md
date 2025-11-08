# PROMPTS PARA ASSISTENTE DE TRANSCRIÇÃO DE CONSULTA

---

## 1. Prompt Genérico

Transcreva este áudio.

---

## 2. Prompt Estruturado (JSON)

```json
{
  "task": "transcrever_e_estruturar_audio_de_consulta",
  "context": {
    "background": "Um médico gravou o áudio de uma consulta e precisa da transcrição para adicionar ao prontuário do paciente.",
    "user_goal": "Transcrever o áudio e, a partir da transcrição, extrair as informações principais da consulta."
  },
  "instructions": {
    "steps": [
      "Transcrever o áudio da consulta na íntegra, identificando o 'Médico' e o 'Paciente'.",
      "A partir da transcrição, criar um resumo no formato SOAP (Subjetivo, Objetivo, Avaliação, Plano).",
      "**Subjetivo:** Resumir a queixa principal do paciente.",
      "**Objetivo:** Listar os dados objetivos mencionados (ex: sinais vitais, resultados de exames físicos).",
      "**Avaliação:** Descrever a hipótese diagnóstica do médico.",
      "**Plano:** Listar os próximos passos, como exames solicitados ou tratamentos prescritos."
    ],
    "output_format": "Documento de texto com duas seções: 'Transcrição Completa' e 'Resumo SOAP'."
  },
  "constraints": [
    "A transcrição deve ser o mais fiel possível ao áudio.",
    "O resumo SOAP deve ser conciso e baseado exclusivamente no conteúdo da transcrição.",
    "**A PRIVACIDADE E A CONFIDENCIALIDADE DOS DADOS DO PACIENTE SÃO PRIORIDADE MÁXIMA.**"
  ],
  "user_input": "[Link para o arquivo de áudio da consulta ou transcrição de texto bruto aqui]"
}
```

---

## 3. Prompt Estruturado (KERNEL)

- **K (Keep it simple):** Transcrever um áudio de consulta e estruturar as informações no formato SOAP.
- **E (Easy to verify):** O resultado deve conter a transcrição completa e as quatro seções do resumo SOAP (S, O, A, P).
- **R (Reproducible results):** O formato SOAP é um padrão médico, garantindo consistência.
- **N (Narrow scope):** A tarefa foca em transcrever e resumir um único áudio.
- **E (Explicit constraints):** Transcrição fiel, resumo conciso, prioridade total à privacidade.
- **L (Logical structure):**

    1.  **Task:** Transcrever um áudio de consulta e gerar um resumo SOAP.
    2.  **Input:** Áudio de uma consulta médica.
    3.  **Constraints:** Identificar 'Médico' e 'Paciente'. Resumo baseado apenas na transcrição. **GARANTIR CONFIDENCIALIDADE.**
    4.  **Output:** Documento com a transcrição completa e o resumo SOAP.
    5.  **Verify:** Checar se a transcrição está completa e se as quatro partes do resumo SOAP foram preenchidas corretamente com base no texto.
