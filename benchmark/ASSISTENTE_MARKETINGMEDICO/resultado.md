# RESULTADO DO BENCHMARK: ASSISTENTE DE MARKETING MÉDICO

Este arquivo documenta os resultados gerados por um modelo de IA para cada um dos três tipos de prompt.

---

## 1. Resposta ao Prompt Genérico

**Prompt:** `Faça o marketing da minha clínica.`

**Resultado:**

Com certeza! Para criar uma estratégia de marketing eficaz e ética para sua clínica, preciso de mais informações:

1.  **Qual é a especialidade da sua clínica?** (Dermatologia, Cardiologia, etc.)
2.  **Quem é seu público-alvo?** (Faixa etária, gênero, interesses, localização)
3.  **Quais serviços ou tratamentos você deseja promover?**
4.  **Qual é o seu principal diferencial?** (Tecnologia, atendimento, corpo clínico)
5.  **Você já possui canais de marketing?** (Site, redes sociais, etc.)

**Muito importante:** Toda a comunicação em marketing médico deve seguir as diretrizes do Conselho Federal de Medicina (CFM) do seu país. As estratégias devem ser focadas em educar e informar, sem prometer resultados ou usar táticas sensacionalistas.

---

## 2. Resposta ao Prompt Estruturado (JSON)

**Prompt:**
```json
{
  "task": "criar_campanha_de_marketing_medico",
  "context": {
    "background": "Uma clínica de dermatologia quer atrair mais pacientes para um novo tratamento de rejuvenescimento facial.",
    "user_goal": "Desenvolver uma campanha de marketing digital de 30 dias para promover o novo tratamento."
  },
  "instructions": {
    "steps": [
      "Definir o público-alvo (ex: mulheres, 40-60 anos, interessadas em estética).",
      "Criar um cronograma de conteúdo para 4 semanas, com 2 posts por semana para Instagram e Facebook.",
      "Sugerir temas para os posts (ex: 'Benefícios do tratamento', 'Antes e Depois', 'Perguntas e Respostas').",
      "Escrever o texto para o primeiro post do Instagram, incluindo uma chamada para 'agendar uma avaliação'.",
      "Sugerir uma ideia para um anúncio pago no Facebook (ex: vídeo curto com um especialista explicando o procedimento)."
    ],
    "output_format": "Documento de planejamento de campanha com seções para cada item."
  },
  "constraints": [
    "Toda a comunicação deve seguir as diretrizes de publicidade do Conselho Federal de Medicina (CFM).",
    "Evitar linguagem que prometa resultados garantidos.",
    "O tom deve ser informativo, profissional e ético."
  ],
  "user_input": "Novo tratamento: 'Lifting a Laser XYZ'. Clínica focada em tecnologia de ponta."
}
```

**Resultado:**

### **Plano de Campanha: Tratamento 'Lifting a Laser XYZ'**

**Aviso:** Todo o conteúdo deve ser revisado pelo Diretor Técnico Médico da clínica antes da publicação para garantir a conformidade com as normas do CFM.

#### **1. Público-Alvo**
*   **Primário:** Mulheres, entre 40 e 65 anos, com interesse em procedimentos estéticos de rejuvenescimento facial não invasivos. Valorizam tecnologia, segurança e resultados de aparência natural.
*   **Secundário:** Homens na mesma faixa etária com preocupações semelhantes sobre envelhecimento da pele.

#### **2. Cronograma de Conteúdo (4 Semanas)**

| Semana | Post 1 (Terça-feira) | Post 2 (Quinta-feira) |
| :--- | :--- | :--- |
| **1** | **Tema:** O que é o 'Lifting a Laser XYZ'? (Educacional) | **Tema:** Para quem é indicado este tratamento? (Informativo) |
| **2** | **Tema:** A tecnologia por trás do procedimento (Foco em segurança e inovação) | **Tema:** Perguntas e Respostas com nosso especialista (Vídeo/Carrossel) |
| **3** | **Tema:** Como o tratamento atua na melhoria da qualidade da pele (Benefícios) | **Tema:** Cuidados pós-procedimento: mitos e verdades |
| **4** | **Tema:** A importância de realizar procedimentos com especialistas qualificados | **Tema:** Conheça nossa estrutura e tecnologia de ponta (Tour virtual/Fotos) |

*Nota: O uso de imagens "Antes e Depois" é proibido pelo CFM. O conteúdo deve ser estritamente educativo.*

#### **3. Texto para o Primeiro Post (Instagram)**

**(Imagem: Foto profissional da clínica ou de um equipamento de laser, com design sóbrio e informativo)**

**Texto:**
Você busca uma pele com aparência mais firme e rejuvenescida? Conheça o 'Lifting a Laser XYZ', uma tecnologia avançada para o tratamento da flacidez e melhora da qualidade da pele.

Este procedimento não invasivo utiliza a energia do laser para estimular a produção natural de colágeno, promovendo um efeito lifting gradual e de aparência natural. É uma opção para quem deseja cuidar da pele com segurança e tecnologia de ponta.

O tratamento é indicado após uma avaliação individual detalhada, onde nosso especialista irá analisar as necessidades da sua pele e esclarecer todas as suas dúvidas.

Quer saber mais sobre como a tecnologia pode ser sua aliada no cuidado com a pele? Agende uma avaliação com nossa equipe médica.

(Link na Bio para agendamento)

**[Nome da Clínica]**
**[CRM do Diretor Técnico]**

#Dermatologia #Rejuvenescimento #TecnologiaLaser #CuidadoComAPele #SaudeDaPele #LiftingALaser #ClinicaDermatologica

#### **4. Ideia para Anúncio Pago (Facebook/Instagram)**
*   **Formato:** Vídeo curto (30-45 segundos).
*   **Conteúdo:** Um dos médicos especialistas da clínica, em um ambiente profissional (consultório), explicando de forma clara e didática:
    1.  O que é o envelhecimento da pele (de forma científica).
    2.  Como a tecnologia do 'Lifting a Laser XYZ' funciona para estimular o colágeno.
    3.  A importância de uma avaliação médica para determinar o tratamento adequado.
*   **CTA (Call to Action):** "Saiba Mais", direcionando para uma página no site da clínica com informações detalhadas e o contato para agendar uma consulta de avaliação. O anúncio deve ser segmentado para o público-alvo definido.

---

## 3. Resposta ao Prompt Estruturado (KERNEL)

**Prompt:**
- **K (Keep it simple):** Criar um plano de campanha de marketing digital para um novo tratamento dermatológico.
- **E (Easy to verify):** O plano deve conter público-alvo, cronograma de 4 semanas, temas de posts, a copy do primeiro post e uma ideia de anúncio.
- **R (Reproducible results):** A estrutura da campanha pode ser replicada para outros tratamentos.
- **N (Narrow scope):** A tarefa foca no planejamento da campanha para um único serviço.
- **E (Explicit constraints):** Seguir as regras do CFM. Não prometer resultados. Tom profissional.
- **L (Logical structure):**
    1.  **Task:** Desenvolver uma campanha de marketing digital de 30 dias para um tratamento dermatológico.
    2.  **Input:** Clínica de dermatologia, novo tratamento 'Lifting a Laser XYZ'.
    3.  **Constraints:** Conformidade com as normas do CFM. Tom ético e informativo.
    4.  **Output:** Documento de planejamento de campanha detalhado.
    5.  **Verify:** Checar se todos os 5 componentes da campanha foram entregues e se as restrições éticas foram consideradas.

**Resultado:**

### **Planejamento de Campanha Digital: Lifting a Laser XYZ**

**Diretriz Principal:** Todo o conteúdo deve ter caráter educativo e informativo, em estrita conformidade com o Manual de Publicidade Médica do CFM.

**1. Público-Alvo Definido:**
Indivíduos (homens e mulheres) acima de 40 anos, preocupados com os sinais de envelhecimento facial como flacidez e perda de qualidade da pele, que buscam soluções tecnológicas seguras e com resultados naturais.

**2. Cronograma de Conteúdo (30 dias):**
*   **Semana 1:** Foco em "O Problema" - Educar sobre o processo de envelhecimento da pele e a perda de colágeno.
*   **Semana 2:** Foco na "Solução Tecnológica" - Apresentar o conceito do laser e como ele estimula o colágeno de forma não invasiva.
*   **Semana 3:** Foco em "Segurança e Expertise" - Destacar a importância da qualificação profissional e da tecnologia aprovada pelos órgãos reguladores.
*   **Semana 4:** Foco em "Próximos Passos" - Explicar como funciona uma consulta de avaliação e os cuidados gerais com a pele.

**3. Temas para Posts:**
*   "Entenda por que nossa pele perde firmeza com o tempo"
*   "O papel do colágeno para uma pele saudável"
*   "Laser na dermatologia: uma abordagem moderna e segura"
*   "5 perguntas frequentes sobre tratamentos a laser"
*   "A importância do diagnóstico médico antes de qualquer procedimento estético"

**4. Copy do Primeiro Post:**
**(Imagem: Ilustração gráfica e sóbria do mecanismo de ação do colágeno na pele)**
**Texto:**
Com o passar dos anos, a produção natural de colágeno em nossa pele diminui, levando à flacidez e ao surgimento de linhas finas. Mas a tecnologia pode ser uma grande aliada.

O 'Lifting a Laser XYZ' é um tratamento que utiliza feixes de luz para aquecer as camadas mais profundas da pele, estimulando o seu corpo a produzir novo colágeno. O resultado é um processo de melhora da firmeza e da textura da pele que ocorre de forma gradual e natural.

É fundamental que qualquer tratamento seja precedido por uma avaliação médica completa.

Converse com nossos especialistas para saber se esta tecnologia é indicada para você.

(Link na Bio para contato)
**[Nome da Clínica] | Dr(a). [Nome do Diretor Técnico] | CRM [Número]**

#DermatologiaAvançada #Colageno #Flacidez #TratamentoALaser #PeleSaudavel

**5. Ideia de Anúncio:**
*   **Formato:** Carrossel de imagens no Instagram.
*   **Sequência:**
    1.  **Card 1:** Pergunta: "Você sabe como a tecnologia pode ajudar a sua pele a produzir mais colágeno?"
    2.  **Card 2:** Infográfico simples mostrando a ação do laser na derme.
    3.  **Card 3:** Foto do equipamento com selo da Anvisa em destaque.
    4.  **Card 4:** Foto do corpo clínico (se permitido e com autorização).
    5.  **Card 5:** CTA: "Agende sua consulta de avaliação e entenda qual o tratamento ideal para sua pele."

Este formato permite passar a informação de forma didática, visual e em total conformidade com as regras do CFM.
