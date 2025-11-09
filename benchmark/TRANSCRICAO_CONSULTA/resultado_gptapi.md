# RESULTADO DO BENCHMARK (SIMULADO GPT): ASSISTENTE DE TRANSCRIÇÃO DE CONSULTA

Este arquivo documenta os resultados simulados de um modelo GPT para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico (Simulação GPT)

**Prompt:** `Transcreva este áudio.`

**Resultado Simulado GPT:**

Com certeza! Posso ajudar a transcrever seu áudio. Para isso, por favor, forneça o arquivo de áudio ou um link para ele.

**Como funciona:**
Eu processaria o áudio, identificaria os diferentes falantes (se houver) e converteria a fala em texto.

**Considerações Importantes sobre Privacidade:**
Se o áudio contiver informações sensíveis, como dados de pacientes em uma consulta médica, é crucial que você tenha todas as permissões e consentimentos necessários para o processamento. A confidencialidade e a segurança dos dados são de sua responsabilidade.

---

## 2. Resposta ao Prompt Estruturado (JSON) (Simulação GPT)

**Prompt:**
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

**Resultado Simulado GPT:**

**Nota:** O link para o arquivo de áudio não foi fornecido. Para demonstrar a capacidade de transcrição e estruturação, segue abaixo um exemplo de uma consulta médica hipotética e seu resumo SOAP.

### **Transcrição Completa da Consulta**

**Médico:** Bom dia, Sra. Ana. O que a traz aqui hoje?

**Paciente:** Bom dia, doutora. Tenho sentido uma dor no joelho direito, já faz umas três semanas. Começou leve, mas agora está mais forte, especialmente quando subo escadas.

**Médico:** Entendo. É uma dor constante ou intermitente?

**Paciente:** Mais constante agora. E sinto que o joelho estala às vezes.

**Médico:** Certo. Vamos examinar. (pausa para exame físico) Há um pouco de inchaço e sensibilidade na patela. A mobilidade está um pouco reduzida na flexão. Não há sinais de trauma recente, correto?

**Paciente:** Não, nenhum trauma.

**Médico:** Ok. Pela descrição e exame, a hipótese mais provável é uma condromalácia patelar. Vou solicitar um raio-x do joelho e uma ressonância magnética para confirmar. Enquanto isso, vou prescrever um anti-inflamatório e fisioterapia. Evite atividades de impacto e retorne em duas semanas com os resultados dos exames.

### **Resumo SOAP da Consulta**

*   **S (Subjetivo):** Paciente, Sra. Ana, relata dor progressiva no joelho direito há 3 semanas, pior ao subir escadas, com estalidos ocasionais. Nega trauma recente.
*   **O (Objetivo):** Exame físico revela leve edema e sensibilidade patelar em joelho direito. Mobilidade reduzida na flexão.
*   **A (Avaliação):** Hipótese diagnóstica: Condromalácia patelar em joelho direito.
*   **P (Plano):**
    1.  Solicitar Raio-X de joelho direito.
    2.  Solicitar Ressonância Magnética (RM) de joelho direito.
    3.  Prescrever anti-inflamatório (ex: Ibuprofeno 400mg, 3x/dia por 7 dias).
    4.  Encaminhamento para fisioterapia.
    5.  Orientar evitar atividades de impacto.
    6.  Retorno em 2 semanas com resultados dos exames.

---

## 3. Resposta ao Prompt Estruturado (KERNEL) (Simulação GPT)

**Prompt:**
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

**Resultado Simulado GPT:**

**Nota:** O áudio da consulta não foi fornecido. Abaixo, um exemplo de transcrição e resumo SOAP para ilustrar a funcionalidade.

#### **Transcrição da Consulta Médica**

*   **Médico:** Boa tarde, Sr. João. Como está se sentindo hoje?
*   **Paciente:** Boa tarde, doutor. Não muito bem. Minha garganta está doendo muito e estou com febre desde ontem à noite.
*   **Médico:** Entendi. Teve tosse ou coriza?
*   **Paciente:** Um pouco de tosse seca, mas a garganta é o pior.
*   **Médico:** Certo. Vou dar uma olhada na sua garganta. (pausa) Está bem avermelhada, com algumas placas. Sua temperatura está em 38.5 graus Celsius. Parece ser uma amigdalite bacteriana. Vou prescrever um antibiótico e um analgésico. Beba bastante líquido e descanse. Retorne se não melhorar em 48 horas.

#### **Resumo SOAP**

*   **Subjetivo:** Paciente, Sr. João, relata dor de garganta intensa e febre (38.5°C) desde a noite anterior. Menciona tosse seca leve.
*   **Objetivo:** Exame físico revela orofaringe hiperemiada com presença de placas. Temperatura aferida em consultório: 38.5°C.
*   **Avaliação:** Amigdalite bacteriana aguda.
*   **Plano:**
    1.  Prescrição de antibiótico (ex: Amoxicilina 500mg, 3x/dia por 7 dias).
    2.  Prescrição de analgésico/antitérmico (ex: Paracetamol 750mg, 3x/dia se dor/febre).
    3.  Orientação para hidratação e repouso.
    4.  Orientação para retorno em 48 horas se não houver melhora.
