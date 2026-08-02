# Superman Suit: A Photovoltaic Neuromuscular Safety Net for Off-World Habitats

## Scientific methodology and research framework

**Document type:** SpaceCHI 2026 position-paper protocol, design-science framework, and supporting computational probe  
**Version:** 2.0  
**Date:** 18 July 2026  
**Proposed maturity:** Integrated concept at approximately TRL 2; subsystem maturity must be assessed separately  
**Primary domain:** Space health countermeasures, wearable systems, human factors, and distributed habitat resilience

---

## SpaceCHI 2026 position-paper frame

### Submission target

This project is positioned as a **SpaceCHI 2026 position paper grounded in design science and Research through Design (RtD)**. The paper proposes a theory-bearing suit concept and a research agenda. It is not positioned as a completed biomedical experiment, a flight-qualified prototype, or a product pitch.

The official SpaceCHI 2026 call states that:

- the conference will take place at NASA Ames Research Center on 24–25 September 2026 with on-site and remote participation;
- position papers are accepted alongside full research papers;
- papers use the Springer proceedings template;
- papers are commonly 5–15 pages excluding references, with no strict page limit;
- review is double-blind;
- review emphasizes relevance, impact, and originality; and
- directly relevant topics include on-body/wearable technology for space health, human–AI interaction, trust in autonomous systems, and human performance [16].

The official deadline is listed as **17 July 2026, 23:59 Anywhere on Earth**, equivalent to **18 July 2026, 18:59 in Bangkok (ICT, UTC+7)**. Submission availability must be checked immediately on the official site; this document does not assume that a portal remains open after the published deadline.

### Recommended paper type

```text
PAPER_TYPE = Position paper
METHOD_FAMILY = Design science + Research through Design
PRIMARY_CONTRIBUTION = Intermediate-level design knowledge
THEORY_BEARING_ARTIFACT = Superman Suit
SUPPORTING_EVIDENCE = Literature grounding + system logic + failure analysis + computational design probe
NOT_CLAIMED = Human efficacy, clinical safety, flight qualification, exercise replacement
TARGET_LENGTH = 8–10 Springer pages excluding references
REVIEW_MODE = Double-blind
```

### Recommended title

**Superman Suit: A Photovoltaic Neuromuscular Safety Net for Off-World Habitats**

More explicitly theoretical alternative:

**Superman Suit: Toward Resource-Aware Physiological Infrastructure for Off-World Habitats**

The term “Superman” is used as a memorable metaphor for protective redundancy, not superhuman enhancement. The paper must state this once to avoid an enhancement-oriented reading.

### Core position

> **Space HCI should treat off-world health garments as distributed, resource-aware physiological infrastructure: systems that can sense local resource availability, preserve a bounded reserve, explain how that reserve is allocated to the body, and maintain limited care when centralized infrastructure is interrupted.**

The Superman Suit makes this position tangible. It proposes a garment that harvests light, stores the resulting electrical energy, and allocates it through user-controlled NMES during temporary interruptions to normal exercise. The artifact is valuable not because it proves that clothing is the best solar generator, nor because NMES replaces exercise, but because it exposes an underdeveloped Space-HCI design problem:

> How should environmental resources, wearable infrastructure, autonomous control, and bodily maintenance relate when every resource is intermittent and every actuation affects a human body?

### Paper-level thesis

The suit should be evaluated as a **metabolic safety net**, not a miniature gym. Its design target is continuity of a limited health-maintenance capability during failure, not equivalence to normal exercise or independence from habitat power under all conditions.

### Position-paper abstract draft

Future off-world habitats may treat the human body as another load on centralized systems for power, exercise, and health maintenance. We argue that Space HCI should also investigate garments as distributed physiological infrastructure: body-proximate systems that harvest local resources, make scarcity legible, and preserve bounded care during infrastructural interruption. We develop this position through the **Superman Suit**, a conceptual photovoltaic garment that stores harvested light energy and allocates it to user-controlled neuromuscular electrical stimulation when ordinary exercise becomes temporarily unavailable. The suit is not proposed as an exercise replacement or flight-ready medical device. Instead, it is a theory-bearing artifact used to examine relationships among environmental intermittency, bodily automation, energy provenance, and crew agency. Following design-science and Research-through-Design traditions, we combine literature grounding, artifact construction, interaction and failure scenarios, and a bounded computational energy probe. We contribute the strong concept of a **metabolic safety net**, a set of design propositions for resource-aware physiological wearables, and a staged research agenda through which the concept can be challenged or falsified. This position reframes off-world clothing from passive equipment or personal electronics into contestable habitat infrastructure and invites the SpaceCHI community to debate where resource allocation ends and bodily governance begins.

### Three principal contributions

1. **A strong concept:** the *metabolic safety net*—a distributed wearable capability that preserves limited physiological maintenance during interruption without claiming to replace primary countermeasures.
2. **A theory-bearing artifact:** the Superman Suit, which materializes a resource-to-body loop and exposes design tensions among autonomy, scarcity, safety, and bodily control.
3. **A design-research agenda:** propositions, boundary conditions, computational probes, human-factors questions, and staged validation methods for resource-aware physiological infrastructure.

### Contribution that is deliberately not claimed

The paper does not contribute evidence that the garment prevents spaceflight muscle atrophy. That is a future empirical question. The position paper contributes a generative design theory, an artifact through which to examine it, and a disciplined route to future evidence.

---

## Design-science and Research-through-Design foundation

### Why design science fits this paper

Design science develops knowledge by constructing and evaluating artifacts that extend human or organizational capabilities [17]. Research through Design in HCI uses the act of making a designed artifact to produce knowledge that is relevant, inventive, and extensible beyond the artifact itself [18]. RtD theory may remain provisional, contingent, and aspirational while still being rigorous when its artifact, process, annotations, and limits are visible [19].

For this paper, “theory” therefore means **intermediate-level design knowledge**, not a universal predictive law. The paper develops strong concepts that are more general than one suit but remain close enough to interaction and use to guide other designs [20].

### Design-science cycles

| Cycle | SpaceCHI application | Evidence or artifact produced |
|---|---|---|
| **Relevance cycle** | Exercise interruptions, resource constraints, maintenance burden, crew autonomy, off-world environmental intermittency | Problem framing and stakeholder tensions |
| **Rigor cycle** | Space health evidence, NMES limitations, wearable PV, human-rated interfaces, medical-device safety, Space HCI | Evidence matrix and claim boundaries |
| **Design cycle** | Construct, annotate, stress-test, and revise the Superman Suit concept | Theory-bearing artifact, scenarios, computation, and propositions |

### Artifact taxonomy

| Design-science artifact type | Output in this paper |
|---|---|
| **Construct** | “Metabolic safety net,” “resource-to-body legibility,” and “bounded bodily automation” |
| **Model** | Environmental resource → harvested energy → stored reserve → controlled physiological allocation → limited maintenance |
| **Method** | Resource-to-body audit and failure-first scenario walkthrough |
| **Instantiation** | Annotated Superman Suit architecture, interface states, and computational energy model |

The instantiation is conceptual and computational. It is not represented as a validated wearable prototype.

### Strong concepts

#### 1. Metabolic safety net

A secondary, distributed system that maintains a bounded physiological-care function when a primary health countermeasure is interrupted.

#### 2. Resource-to-body legibility

The wearer can understand the origin, quantity, uncertainty, and intended bodily use of a resource before actuation occurs.

#### 3. Bounded bodily automation

Autonomous scheduling or adaptation can operate only inside explicit physiological, operational, and user-approved limits. The system cannot silently initiate or escalate bodily actuation.

#### 4. Graceful physiological degradation

When energy, sensing, or infrastructure deteriorates, the system reduces or postpones capability visibly and safely instead of hiding shortfall or increasing stimulation risk.

#### 5. Contingency over substitution

The value of the wearable is measured by continuity during interruption, not by whether it reproduces every benefit of the primary system.

### Design propositions

**DP1 — Distributed continuity:** Off-world health systems should preserve a minimum distributed care capability so that bodily maintenance does not disappear completely when centralized equipment fails.

**DP2 — Provenance before actuation:** A resource-aware wearable should disclose where its energy came from, how much is available, what uncertainty remains, and what bodily action that energy can support.

**DP3 — Bodily sovereignty:** Any system that actuates the body should require preview, affirmative initiation, immediate local stop, and intelligible post-action accounting.

**DP4 — Safe scarcity:** Energy scarcity should reduce, defer, or cancel functionality; it must never justify exceeding an approved stimulation or discomfort envelope.

**DP5 — Countermeasure plurality:** A physiological wearable should be designed as one layer in a portfolio of countermeasures, not as a totalizing replacement for exercise, clinical care, or habitat infrastructure.

**DP6 — Failure-first evaluation:** Resource-aware physiological systems should be evaluated through outages, uncertainty, sensor disagreement, and user refusal—not only through nominal operation.

**DP7 — Evidence-bound speculation:** Speculative artifacts become scientifically useful when every claim is labeled as established evidence, design inference, computational result, or future empirical question.

### Paper research questions

**PRQ1:** What conceptual shift occurs when an off-world health garment is treated as physiological infrastructure rather than personal equipment?

**PRQ2:** How can a speculative but technically grounded suit expose tensions among intermittent resources, bodily automation, safety, and crew agency?

**PRQ3:** Which intermediate-level design concepts can transfer from the Superman Suit to other resource-aware space wearables?

**PRQ4:** How can a lightweight computational probe discipline the material plausibility of a position paper without being mistaken for physiological validation?

**PRQ5:** What staged research programme would be required to accept, narrow, or reject the metabolic-safety-net proposition?

---

## Position-paper evidence architecture

### Four evidence classes

Every important statement must be assigned one class in the internal claim ledger.

| Code | Evidence class | Example | Allowed language |
|---|---|---|---|
| `E` | Established external evidence | NMES can evoke contraction; ISS uses exercise countermeasures | “Prior work shows…” |
| `D` | Design inference | A garment can make energy provenance body-proximate and visible | “We propose/argue…” |
| `C` | Computational design-probe result | EAR distribution under declared assumptions | “Our model suggests…” |
| `F` | Future empirical question | Muscle preservation during a real outage | “Future work must test…” |

An AI agent must never convert `D`, `C`, or `F` into `E` during editing.

### Claim-ledger pseudocode

```text
FOR each manuscript claim:
    ASSIGN evidence_class in [E, D, C, F]
    ATTACH source_or_artifact
    ATTACH scope_boundary
    ATTACH strongest_allowed_wording
    ATTACH falsification_condition

IF evidence_class == E AND no source exists:
    DOWNGRADE to D or F

IF evidence_class == C:
    REQUIRE assumptions + uncertainty + model limitation nearby

IF claim contains ["proves", "safe", "effective", "flight-ready", "replaces"]:
    REQUIRE direct matching evidence
    OTHERWISE rewrite conservatively
```

### The suit as a boundary object

The artifact should allow several communities to interrogate the same design from different positions:

- space-health researchers: Is the proposed physiological target meaningful?
- power engineers: Under what illumination and storage conditions is it plausible?
- wearable designers: Why must harvesting, sensing, and actuation be clothing?
- human-factors researchers: Can the user understand and stop the system?
- mission planners: Does distributed redundancy justify mass and maintenance?
- ethicists: Who controls bodily actuation and health-data interpretation?
- HCI theorists: What changes when a garment becomes infrastructure?

The paper succeeds if it enables productive disagreement across these views. Consensus that the artifact is ready for deployment is not required.

### Role of the 30-minute computation

The computation is an **evaluative design probe**, not the paper's central experiment. It performs three functions:

1. prevents the paper from assuming that “solar powered” automatically means energy sufficient;
2. identifies which material assumptions most constrain the concept; and
3. demonstrates evidence-bound speculation by allowing autonomous, assisted, or unsupported outcomes.

The result should occupy approximately one page or less in the position paper. Full pseudocode and tables remain supplementary material.

### Completed probe result — 18 July 2026

The supporting computational probe was completed using 750,000 Monte Carlo observations: 50,000 draws for each of five illustrative illumination scenarios crossed with three candidate NMES electrical-load profiles. All 12 pre-run model tests passed. An initial post-run audit exposed a unit-name checker defect, which was corrected without changing the model or numeric outputs; all 17 post-run tests then passed.

The result deliberately did not produce a universal autonomy claim:

- 9 of 15 scenario–protocol pairs met the probe's preliminary energy-support rule;
- 1 was conditional and assumption-sensitive;
- 4 supported only PV-assisted framing; and
- 1 did not support energy autonomy.

Deployed or strongly illuminated scenarios were robust under the declared assumptions. Indoor operation was conditional or assisted, while interrupted-light operation was predominantly assisted or unsupported. Irradiance and charging duration were the leading positive sensitivity drivers, and electronics overhead was a recurrent negative driver. All zero-light boundary cases failed, and all deliberate voltage-compliance stress cases exceeded the assumed output envelope.

The position-paper implication is not that the suit “works.” It is that the garment must be theorized as **context-dependent physiological infrastructure** capable of autonomous, hybrid, or unavailable states, with resource provenance and graceful degradation made visible to the wearer.

See the [concise probe summary](spacechi_position_paper/probe_summary.md) and [complete scientific report](computer_experiment/runs/20260718T023119Z_seed_20260718/report.md).

---

## Position-paper research protocol for an AI-led workflow

### Protocol overview

| Phase | Purpose | AI-led work | Human decision required |
|---|---|---|---|
| P0 — Position lock | Fix the arguable claim and venue fit | Draft thesis variants and scope exclusions | Select thesis/title or stop |
| P1 — Rigor and claim audit | Separate evidence from inference | Build evidence matrix and claim ledger | Approve claim boundaries |
| P2 — Artifact construction | Make the theory visible | Produce architecture, states, scenarios, and annotations | Approve artifact coherence |
| P3 — Computational design probe | Stress-test energy plausibility | Run the 30-minute computer-only protocol | Include, revise, or omit probe |
| P4 — Theory synthesis | Extract transferable knowledge | Derive strong concepts, propositions, tensions, and research agenda | Approve theory contribution |
| P5 — Manuscript assembly | Build anonymous Springer paper | Draft, cite, shorten, and cross-check | Approve manuscript wording |
| P6 — Submission audit | Verify venue compliance | Check anonymity, format, originality, and files | Human alone authorizes submission |

### Position-paper workflow artifacts

The agent creates new versioned files and never overwrites an approved version:

```text
spacechi_position_paper/
├── decision_log.md
├── venue_requirements.md
├── evidence_matrix.csv
├── claim_ledger.md
├── artifact_spec.md
├── design_scenarios.md
├── design_propositions.md
├── probe_summary.md
├── research_agenda.md
├── reviewer_challenge_matrix.md
├── manuscript_v01.md
└── submission_checklist.md
```

Every human gate is appended to `decision_log.md` with timestamp, selected option, requested change, and affected artifact version.

### Master position-paper pseudocode

```text
PROCEDURE BUILD_SPACECHI_2026_POSITION_PAPER:
    READ official SpaceCHI 2026 submission page
    RECORD access date and current requirements
    DO NOT assume a portal is open; ask human to verify

    CALL P0_POSITION_LOCK
    HUMAN_DECISION_REQUIRED P0_GATE:
        OPTIONS = [SELECT_RECOMMENDED_POSITION, SELECT_ALTERNATIVE, EDIT, STOP]
    IF STOP: TERMINATE

    CALL P1_RIGOR_AND_CLAIM_AUDIT
    HUMAN_DECISION_REQUIRED P1_GATE:
        OPTIONS = [APPROVE_BOUNDARIES, REQUEST_CORRECTION, STOP]
    IF REQUEST_CORRECTION: REVISE_LEDGER_WITH_AUDIT_TRAIL
    IF STOP: TERMINATE

    CALL P2_ARTIFACT_CONSTRUCTION
    HUMAN_DECISION_REQUIRED P2_GATE:
        OPTIONS = [APPROVE_ARTIFACT, REVISE_INTERACTION, REVISE_SCOPE, STOP]
    IF revision requested: APPLY_AND_RECHECK_CLAIM_LEDGER
    IF STOP: TERMINATE

    CALL P3_COMPUTATIONAL_DESIGN_PROBE
    HUMAN_DECISION_REQUIRED P3_GATE:
        OPTIONS = [INCLUDE_AS_SUPPORT, INCLUDE_AS_NEGATIVE_RESULT, REVISE_ONCE, OMIT]
    NEVER hide a negative result by rerunning until favorable

    CALL P4_THEORY_SYNTHESIS
    HUMAN_DECISION_REQUIRED P4_GATE:
        OPTIONS = [APPROVE_PROPOSITIONS, MERGE, DELETE, REWRITE]
    REQUIRE at least one contestable position and one falsification condition

    CALL P5_MANUSCRIPT_ASSEMBLY
    HUMAN_DECISION_REQUIRED P5_GATE:
        OPTIONS = [APPROVE_DRAFT, REQUEST_ONE_REVISION_ROUND, REJECT]
    PRESERVE previous draft

    CALL P6_SUBMISSION_AUDIT
    HUMAN_DECISION_REQUIRED P6_GATE:
        OPTIONS = [AUTHORIZE_MANUAL_SUBMISSION, HOLD, ABANDON]
    AI_AGENT MUST NOT submit externally without explicit human authorization
```

---

## Position Phase P0 — Position and venue lock

### START condition

- SpaceCHI 2026 requirements have been checked against the official page.
- The paper is not simultaneously under review elsewhere.
- The author understands that a position paper advances an arguable view rather than pretending to report completed validation.

### AI actions

```text
GENERATE three thesis statements
RANK them on relevance, originality, impact, contestability, and evidence fit
RECOMMEND one title and one subtitle
WRITE explicit non-claims
WRITE one-sentence answer to "Why SpaceCHI?"
WRITE one-sentence answer to "Why now?"
```

### END condition

- One position statement is selected.
- Title and intended contribution are stable.
- Non-claims are visible.

### HUMAN_DECISION_REQUIRED P0_GATE

The human selects or edits the thesis and title. This decision cannot be delegated because it defines the author's scholarly position.

---

## Position Phase P1 — Rigor and claim audit

### START condition

- P0 position is approved.

### AI actions

```text
CREATE spacechi_position_paper/evidence_matrix.csv
CREATE spacechi_position_paper/claim_ledger.md

FOR each major claim:
    LABEL E, D, C, or F
    LINK source or artifact
    STATE limitation
    STATE allowed wording
    STATE what observation would weaken it

CHECK especially:
    exercise remains primary countermeasure
    NMES limitation versus exercise
    EasyMotion and adjacent garment precedents
    wearable-PV feasibility versus mission sufficiency
    light intermittency on Moon/Mars
    user control and human-rated interface requirements
```

### END condition

- No major factual claim lacks a source.
- No design inference is presented as empirical fact.
- The computational probe has a separate evidence class.

### HUMAN_DECISION_REQUIRED P1_GATE

The human approves the paper's evidence boundary or asks for specific corrections.

---

## Position Phase P2 — Theory-bearing artifact construction

### START condition

- Claim ledger is approved.

### Required artifact views

1. **Resource-flow view:** light → conversion → storage → allocation → body.
2. **Interaction-state view:** off → self-check → preview → user consent → stimulation/rest → stop/fault → accounting.
3. **Habitat-role view:** central exercise as primary; garment as contingency layer.
4. **Failure view:** shadow, low storage, electrode fault, sensor disagreement, user refusal, and central outage.
5. **Agency view:** what the wearer, clinician, controller, and habitat system may each decide.

### AI actions

```text
CREATE artifact_spec.md
CREATE one annotated architecture figure specification
CREATE one nominal-use scenario
CREATE two failure scenarios
CREATE one refusal scenario where user cancels without penalty
ANNOTATE every feature with the design proposition it embodies
REMOVE any feature that exists only for futuristic appearance
```

### END condition

- The suit visibly carries the theory.
- Every component supports a proposition, scenario, or safety boundary.
- The artifact can be understood without claiming a built prototype.

### HUMAN_DECISION_REQUIRED P2_GATE

The human approves whether the artifact is coherent, revises its interaction, narrows its scope, or stops.

---

## Position Phase P3 — Computational design probe

### START condition

- Artifact energy boundary is stable.
- P2 has been approved.

### AI actions

Execute the later section titled **Supporting design probe: 30-minute computer-only experiment**. Interpret the run only through its internal rules.

```text
IF probe result supports a declared scenario:
    INCLUDE as bounded material plausibility
ELSE IF result is conditional or PV-assisted:
    INCLUDE as a productive narrowing of the concept
ELSE IF result rejects autonomy:
    REFRAME suit as hybrid or use negative result to challenge the position
ELSE IF run is invalid:
    OMIT numeric claim and disclose that the probe was inconclusive
```

### END condition

- The paper has either a bounded computational result or an explicit reason for omitting it.
- The design position does not depend on a favorable result.

### HUMAN_DECISION_REQUIRED P3_GATE

The human decides whether to include the probe as support, include it as a negative result, authorize one principled revision, or omit it. Rerunning solely to obtain a favorable result is prohibited.

---

## Position Phase P4 — Reflective theory synthesis

### START condition

- Artifact and probe decisions are fixed.

### AI actions

```text
COMPARE artifact behavior across nominal, outage, scarcity, fault, and refusal cases
IDENTIFY recurring interaction ideas
ABSTRACT them into strong concepts
FORMULATE design propositions in contestable language
FOR each proposition:
    LINK supporting artifact feature
    LINK evidence class
    STATE boundary condition
    STATE falsification or revision condition
    STATE transfer case beyond the Superman Suit

CREATE design_propositions.md
CREATE research_agenda.md
```

### Reflection questions

- What became visible only after making the suit concept?
- Which part of the position survives if photovoltaic autonomy fails?
- What does the garment distribute: energy, control, risk, responsibility, or all four?
- When does bodily automation become bodily governance?
- What must remain centralized even in a distributed habitat?
- Which proposition transfers to nutrition, thermal regulation, rehabilitation, or life-support wearables?

### END condition

- The contribution extends beyond the single artifact.
- Propositions are generative but bounded.
- Negative probe findings have influenced the theory rather than being hidden.

### HUMAN_DECISION_REQUIRED P4_GATE

The human approves, merges, removes, or rewrites the propositions. These express the author's intellectual contribution and cannot be selected solely by the agent.

---

## Position Phase P5 — Manuscript assembly

### START condition

- Position, evidence boundary, artifact, probe status, and propositions are approved.

### Recommended 8–10-page architecture

| Section | Target space | Function |
|---|---:|---|
| Abstract | 200–250 words | Position, artifact, method, and contributions |
| 1. The position | 0.75 page | State the provocation immediately |
| 2. Why a safety net is needed | 1.0 page | Ground the problem and reject exercise-replacement framing |
| 3. Design-science framing | 1.0 page | Explain theory-bearing artifact and RtD method |
| 4. Superman Suit | 1.5–2.0 pages | Architecture, interaction states, and scenarios |
| 5. Computational design probe | 0.75–1.0 page | Material plausibility and limits |
| 6. Design propositions | 1.5 pages | Transferable intermediate-level knowledge |
| 7. Research and ethics agenda | 1.0 page | Future studies, bodily agency, and governance |
| 8. Discussion and conclusion | 0.75 page | SpaceCHI debate and take-away |

### AI actions

```text
CREATE anonymous Springer-compatible manuscript draft
LEAD with the position, not a literature-review chronology
USE the suit as a running artifact throughout the paper
KEEP computational method proportional to supporting role
MOVE full equations, pseudocode, and extended tables to supplement
INCLUDE exactly three headline contributions
INCLUDE limitations before conclusion
INCLUDE two explicit questions for SpaceCHI community discussion
RUN claim-ledger audit after every revision
REMOVE author identity, acknowledgements, self-identifying links, and metadata
```

### END condition

- Manuscript reads as a position paper.
- The artifact and propositions are central.
- Evidence classes remain intact.
- Formatting and anonymity checks pass.

### HUMAN_DECISION_REQUIRED P5_GATE

The human approves the scholarly voice and wording or requests one revision round.

---

## Position Phase P6 — Submission audit

### START condition

- Human has approved the draft.

### AI checks

```text
VERIFY official deadline and portal state
VERIFY Springer template
VERIFY double-blind anonymization
VERIFY title/abstract/keywords
VERIFY 5–15-page norm or justified length
VERIFY every figure permission and caption
VERIFY references and DOI links
VERIFY no concurrent submission
VERIFY LLM-use disclosure requirement with current venue policy
VERIFY PDF accessibility and embedded fonts
VERIFY supplementary files contain no identity leak
WRITE submission_checklist.md
DO NOT click final submit
```

### END condition

- A pass/fail checklist exists.
- All unresolved issues are visible.
- No external submission has occurred.

### HUMAN_DECISION_REQUIRED P6_GATE

Only the human author may authorize submission, hold the paper, or abandon it.

---

## Reviewer-challenge matrix

| Likely challenge | Position-paper response |
|---|---|
| “Why not use the habitat grid?” | The paper does not claim PV universally outperforms the grid. It uses point-of-use harvesting to examine distributed resilience, energy provenance, and resource-to-body interaction. |
| “NMES cannot replace exercise.” | Agreed. The strong concept is a contingency layer precisely because NMES is partial. |
| “There is no flight-ready suit.” | Correct. This is a design-science position paper; the artifact generates and organizes design knowledge and a future validation agenda. |
| “The concept is speculative.” | It is deliberately speculative but evidence-bound: adjacent components exist, assumptions are explicit, failure cases are central, and the computational probe can reject autonomy. |
| “Sunlight is unreliable.” | Intermittency is a core design condition, not an omitted inconvenience. The suit may be autonomous, PV-assisted, hybrid, or infeasible depending on context. |
| “Why a garment?” | Clothing supplies a body-conformal interface for sensing, electrodes, explanation, and immediate control while also offering a deployable surface. The paper treats this as a design inference to be challenged. |
| “Is bodily automation ethical?” | The paper foregrounds consent, local stop, provenance, refusal, and role boundaries as theoretical contributions rather than treating them as implementation details. |
| “Superman implies enhancement.” | The metaphor refers to a safety net. The paper explicitly rejects enhancement and exercise-replacement claims. |

### SpaceCHI discussion questions

1. If garments become habitat infrastructure, which resource-allocation decisions should remain with the wearer, which may be delegated to automation, and which belong to mission or medical authority?
2. Should distributed physiological systems be judged by efficiency, continuity, bodily agency, or a new combination of all three?

---

## Supporting design probe: 30-minute computer-only experiment

### Rapid experiment status

> **This is a supporting design probe, not the paper's primary contribution.** It is a computational feasibility and claim-stress test. It uses no human participant, no NMES hardware, no photovoltaic hardware, and no medical intervention. It can test whether the proposed energy chain is mathematically plausible under declared assumptions. It cannot demonstrate muscle preservation, comfort, clinical safety, or flight readiness.

The long-term scientific framework remains below this section as the future validation programme. Results from the rapid experiment may refine that programme but cannot replace its human, hardware, or environmental studies.

### Rapid research question

Under explicitly declared uncertainty ranges, in which illumination and charging scenarios could a garment-scale photovoltaic system supply the electrical energy required by a candidate NMES contingency protocol?

### Rapid hypotheses

**CH1 — Energy sufficiency:** At least one deployed-light scenario will produce a positive daily energy margin for the candidate NMES protocol.

**CH2 — Context dependence:** Indoor or heavily interrupted light will produce lower energy-autonomy probability than deployed direct-light scenarios.

**CH3 — Dominant variables:** Irradiance, exposed PV area, charging duration, total electronics overhead, and stimulation-session count will dominate uncertainty in the energy-autonomy ratio.

**CH4 — Claim boundary:** At least one apparently favorable scenario will fail when electrical output-voltage compliance and lower-tail uncertainty are included, demonstrating why best-case arithmetic is insufficient.

### What this experiment can and cannot conclude

| Permitted conclusion | Prohibited conclusion |
|---|---|
| “Energy autonomy is computationally plausible under scenario X and the declared assumptions.” | “The suit preserves muscle.” |
| “The system is more accurately described as PV-assisted under scenario Y.” | “The NMES regimen is safe or tolerable.” |
| “Variable Z dominates modeled energy uncertainty.” | “The suit works on the Moon or Mars.” |
| “The assumed stimulator may be voltage-compliance limited in N% of model draws.” | “A simulated current produces the required human contraction.” |
| “These assumptions need physical measurement next.” | “The device is medically or operationally ready.” |

### Primary computational endpoint

For every illumination-scenario × NMES-protocol pair:

$$
P\left(EAR \ge 1.20\;\land\;V_{required}\le V_{compliance}\right)
$$

where $EAR$ is the energy-autonomy ratio and the factor 1.20 represents a **screening reserve**, not a clinical or flight-certification threshold.

### Secondary computational endpoints

- median, 5th percentile, and 95th percentile EAR;
- probability that $EAR \ge 1.00$;
- probability that the requested current is within stimulator voltage compliance;
- median harvested Wh/day and system Wh/day;
- median fraction of demand supplied by PV, capped at 100% for reporting;
- minimum usable storage capacity for one day of operation with the 1.20 reserve;
- break-even exposed area and charging duration;
- estimated sessions supported per charging window; and
- ranked correlation of each uncertain input with $\log_{10}(EAR)$.

### Computer-only model boundary

```text
Modeled:
incident light → PV output → MPPT/storage losses → stored Wh
candidate NMES waveform + device overhead → required Wh
stored Wh / required Wh → energy-autonomy ratio
current × impedance → required compliance voltage

Not modeled as evidence:
motor-unit recruitment, evoked torque, pain, skin response, muscle fatigue,
muscle preservation, battery fire propagation, lunar dust physics, radiation,
thermal-vacuum behavior, flight operations, or medical-device certification
```

### Required output artifacts

The executing agent must create a new timestamped directory and must not overwrite an earlier run:

```text
computer_experiment/
└── runs/
    └── <UTC_TIMESTAMP>_seed_<SEED>/
        ├── README.md
        ├── assumptions.json
        ├── environment.txt
        ├── run_experiment.py
        ├── test_experiment.py
        ├── raw_results.csv
        ├── scenario_summary.csv
        ├── sensitivity.csv
        ├── summary.json
        ├── report.md
        ├── run.log
        └── SHA256SUMS.txt
```

Optional plots may be created only if a plotting library is already installed. Missing plotting software must not delay or invalidate the experiment.

### Fixed 30-minute schedule

| Phase | Clock time | AI-agent responsibility | Required human decision |
|---|---:|---|---|
| Phase 0 — Scope lock | 00:00–02:00 | Restate scope, protect files, initialize run ID | Approve computer-only scope or stop |
| Phase 1 — Assumption lock | 02:00–07:00 | Inspect environment and prepare bounded assumptions | Approve, edit, or reject assumptions |
| Phase 2 — Build and execute | 07:00–18:00 | Write dependency-light model and tests; run Monte Carlo | Accept run validity, request one rerun, or stop |
| Phase 3 — Stress test | 18:00–23:00 | Perform sensitivity, boundary, and break-even analyses | Approve interpretation category or mark inconclusive |
| Phase 4 — Report | 23:00–28:00 | Generate reproducible report and artifact hashes | Approve wording, request one correction, or reject |
| Phase 5 — Close | 28:00–30:00 | Freeze artifacts and print concise handoff | Decide archive/retain or mark failed |

If a phase exceeds its budget, the agent must preserve completed artifacts, skip optional plots, and continue to the next human gate. It must never hide that a test or analysis was skipped.

### Copy-paste launch instruction for the executing AI agent

```text
Read Superman_Suit_Research_Framework.md completely, then execute only the
section titled "Supporting design probe: 30-minute computer-only experiment."

Follow the Agent execution contract exactly. Begin with Rapid Phase 0 only.
Do not run Phase 1 until I answer HUMAN_DECISION_REQUIRED H0. Pause after every
phase for its human decision gate. Use a new timestamped directory under
computer_experiment/runs and preserve all existing files. The experiment is a
computer-only energy-feasibility screen; do not involve a person or physical
NMES/PV hardware, and do not make efficacy, medical-safety, or flight-readiness
claims. Keep the total run within 30 minutes and report any skipped step.
```

---

## Agent execution contract

### Agent role

The executing AI agent acts as a **computational research assistant**, not as a clinician, principal investigator, or safety certifier.

### Hard constraints

```text
CONSTRAINT C01: Total wall-clock target = 30 minutes.
CONSTRAINT C02: Use this computer only; do not recruit or stimulate a person.
CONSTRAINT C03: Do not connect to, control, or claim evidence from physical NMES/PV hardware.
CONSTRAINT C04: Preserve existing files. Create a new timestamped run directory.
CONSTRAINT C05: Use deterministic pseudorandom sampling with a recorded seed.
CONSTRAINT C06: Prefer Python standard library; use installed packages only when optional.
CONSTRAINT C07: Record every assumption with unit, low, mode, high, and rationale/status.
CONSTRAINT C08: Label illustrative values as assumptions, not measurements.
CONSTRAINT C09: Pause at every HUMAN_DECISION_REQUIRED gate.
CONSTRAINT C10: Do not continue after human selects STOP or REJECT.
CONSTRAINT C11: Do not convert model output into a medical, efficacy, or flight-readiness claim.
CONSTRAINT C12: On error, preserve logs and report FAILED or INCONCLUSIVE; do not fabricate output.
```

### Master pseudocode

```text
PROCEDURE RUN_30_MINUTE_SUPERMAN_SUIT_EXPERIMENT:
    SET experiment_name = "PV-to-NMES computational feasibility screen"
    SET time_limit_minutes = 30
    SET default_seed = 20260718
    SET default_draws = 50000
    SET optional_draws_after_timeout = 10000

    START_TIMER()

    CALL PHASE_0_SCOPE_LOCK()
    HUMAN_DECISION_REQUIRED H0:
        QUESTION = "Approve computer-only energy-feasibility scope?"
        OPTIONS = [APPROVE, MODIFY_SCOPE, STOP]
    IF H0 == STOP:
        WRITE_STOP_REPORT(reason="Scope not approved")
        TERMINATE
    IF H0 == MODIFY_SCOPE:
        APPLY_ONLY_CHANGES_THAT_REMAIN_COMPUTER_ONLY_AND_NON_CLINICAL
        REPEAT H0

    CALL PHASE_1_ASSUMPTION_LOCK()
    HUMAN_DECISION_REQUIRED H1:
        QUESTION = "Approve the scenario and protocol assumption ranges?"
        OPTIONS = [APPROVE_DEFAULTS, EDIT_VALUES, REMOVE_SCENARIO, STOP]
    IF H1 == STOP:
        WRITE_STOP_REPORT(reason="Assumptions not approved")
        TERMINATE
    IF H1 in [EDIT_VALUES, REMOVE_SCENARIO]:
        VALIDATE_HUMAN_CHANGES
        SAVE_NEW_ASSUMPTION_VERSION
        REPEAT H1

    CALL PHASE_2_BUILD_AND_EXECUTE()
    HUMAN_DECISION_REQUIRED H2:
        QUESTION = "Tests passed and run provenance is complete. Accept this run?"
        OPTIONS = [ACCEPT, RERUN_ONCE_WITH_NEW_SEED, STOP_AS_FAILED]
    IF H2 == RERUN_ONCE_WITH_NEW_SEED:
        SET seed = HUMAN_VALUE_OR(default_seed + 1)
        CALL PHASE_2_BUILD_AND_EXECUTE(rerun=true)
        REPEAT H2
    IF H2 == STOP_AS_FAILED:
        MARK_RUN_FAILED
        TERMINATE

    CALL PHASE_3_STRESS_TEST_AND_INTERPRET()
    HUMAN_DECISION_REQUIRED H3:
        QUESTION = "Select the allowed interpretation for each scenario."
        OPTIONS = [PRELIMINARY_SUPPORT, CONDITIONAL_ONLY, PV_ASSISTED, NOT_SUPPORTED, INCONCLUSIVE]
    RECORD_H3_WITHOUT_CHANGING_NUMERIC_RESULTS

    CALL PHASE_4_REPORT()
    HUMAN_DECISION_REQUIRED H4:
        QUESTION = "Approve report wording and limitations?"
        OPTIONS = [APPROVE, ONE_CORRECTION, REJECT]
    IF H4 == ONE_CORRECTION:
        APPLY_CORRECTION_WITH_AUDIT_NOTE
        REGENERATE_REPORT_AND_HASHES
        REPEAT H4
    IF H4 == REJECT:
        MARK_REPORT_REJECTED_BUT_KEEP_ARTIFACTS

    CALL PHASE_5_CLOSE()
    HUMAN_DECISION_REQUIRED H5:
        QUESTION = "Retain this run as the project baseline?"
        OPTIONS = [RETAIN_BASELINE, RETAIN_AS_EXPLORATORY, MARK_FAILED]
    RECORD_FINAL_HUMAN_DECISION
    FREEZE_MANIFEST
    PRINT_FINAL_HANDOFF
    TERMINATE
```

---

## Rapid Phase 0 — Scope lock

### START condition

- The agent can read this Markdown file.
- The workspace path is known.
- No human or hardware procedure has begun.

### Automated actions

```text
PROCEDURE PHASE_0_SCOPE_LOCK:
    READ this Markdown section completely
    DECLARE scope = "computer-only PV-to-NMES energy feasibility"
    DECLARE excluded_claims = [human efficacy, human safety, comfort, flight readiness]
    RESOLVE workspace path
    VERIFY existing project files will not be overwritten
    CREATE parent directory "computer_experiment/runs" if absent
    CREATE run_id from UTC timestamp and seed
    CREATE new run directory only if it does not already exist
    WRITE README.md with scope, exclusions, start time, agent identity, and status="INITIALIZED"
    PRINT concise scope statement for human
```

### END condition

- A unique run directory exists.
- Existing artifacts remain untouched.
- Scope and prohibited claims are recorded.

### HUMAN_DECISION_REQUIRED H0

The human approves the computer-only scope, modifies it without adding human/hardware testing, or stops the run.

---

## Rapid Phase 1 — Environment and assumption lock

### START condition

- H0 = APPROVE.
- Run directory status = `INITIALIZED`.

### Automated environment inspection

```text
PROCEDURE INSPECT_ENVIRONMENT:
    RECORD operating system and architecture
    RECORD Python version
    RECORD current UTC time and timezone
    RECORD available disk space for run directory
    CHECK whether matplotlib is installed; label OPTIONAL_TRUE or OPTIONAL_FALSE
    CHECK whether current workspace is under version control; do not mutate repository state
    WRITE all results to environment.txt
    REQUIRE Python >= 3.9 OR mark BLOCKED
```

### Default scenario assumptions

All values below are **illustrative triangular-distribution inputs** for computational screening. They are not measured mission-environment values. The human must approve or edit them at H1.

| Scenario ID | Reference irradiance W/m²: low / mode / high | Charging duration h: low / mode / high | Geometry factor: low / mode / high | Transmission/shading factor: low / mode / high | Interpretation |
|---|---:|---:|---:|---:|---|
| `INDOOR_HABITAT` | 1 / 5 / 15 | 2 / 6 / 12 | 0.40 / 0.75 / 1.00 | 0.60 / 0.90 / 1.00 | Artificial-light screening case |
| `WINDOW_FILTERED` | 50 / 250 / 700 | 0.5 / 2 / 6 | 0.25 / 0.60 / 0.90 | 0.50 / 0.80 / 0.95 | Sunlit but filtered/oblique case |
| `LUNAR_DEPLOYED_SUN` | 1000 / 1300 / 1365 | 0.25 / 1 / 3 | 0.50 / 0.85 / 1.00 | 0.80 / 0.95 / 1.00 | Deployed direct-light screening case |
| `MARS_CLEAR_DEPLOYED` | 150 / 400 / 650 | 0.5 / 2 / 5 | 0.40 / 0.75 / 0.95 | 0.50 / 0.80 / 0.95 | Clear-to-moderately-dusty screening case |
| `LIGHT_INTERRUPTION` | 0 / 5 / 50 | 0 / 1 / 4 | 0.10 / 0.40 / 0.80 | 0.10 / 0.40 / 0.80 | Shadow, storm, or no-access stress case |

### Shared PV and power-chain assumptions

| Variable | Unit | Low | Mode | High | Status |
|---|---:|---:|---:|---:|---|
| Exposed PV area | m² | 0.15 | 0.30 | 0.45 | Illustrative garment/deployable range |
| PV conversion efficiency | fraction | 0.08 | 0.14 | 0.22 | Illustrative technology range |
| MPPT efficiency | fraction | 0.80 | 0.90 | 0.96 | Illustrative |
| Storage charge/discharge efficiency | fraction | 0.75 | 0.88 | 0.95 | Illustrative |

The energy-margin decision threshold is fixed at $EAR=1.20$ for this rapid screen. It is not sampled and is not a medical, regulatory, or flight threshold.

### Candidate NMES protocol assumptions

The rapid experiment compares three energy-load profiles. None is a clinical prescription.

| Protocol ID | Sessions/day | Minutes/session | Simultaneous channels | Purpose |
|---|---:|---:|---:|---|
| `BRIDGE_LIGHT` | 1 | 30 | 2 | Low-demand contingency screen |
| `HANSEN_ANCHORED` | 3 | 30 | 2 | Energy screen anchored to the published 3 × 30-minute quadriceps schedule [3] |
| `MULTICHANNEL_SCREEN` | 1 | 45 | 4 | Exploratory multichannel garment load |

Shared uncertain NMES-device inputs:

| Variable | Unit | Low | Mode | High | Notes |
|---|---:|---:|---:|---:|---|
| Commanded current | A | 0.03 | 0.06 | 0.10 | Model input only; not a prescription |
| Electrode-path impedance | Ω | 300 | 500 | 1000 | Simplified electrical load |
| Stimulator compliance voltage | V | 80 | 100 | 120 | Requested voltage above this is flagged |
| Pulse width per phase | s | 0.00030 | 0.00040 | 0.00050 | Biphasic model |
| Phases per pulse | count | 2 | 2 | 2 | Fixed |
| Pulse frequency | Hz | 35 | 60 | 80 | Candidate range |
| Train ON time | s | 5 | 5 | 7 | Candidate range |
| Train OFF time | s | 10 | 10 | 15 | Candidate range |
| Output-stage efficiency | fraction | 0.60 | 0.80 | 0.92 | Simplified |
| Controller/sensor/interface power | W | 0.20 | 0.60 | 1.50 | Includes non-stimulation loads |

### Sampling rules

```text
FOR each Monte Carlo draw:
    SAMPLE continuous variables from triangular(low, high, mode)
    KEEP protocol counts and phases_per_pulse fixed as declared
    CLAMP every efficiency and factor to [0, 1]
    REJECT any non-finite or negative sample
    RECORD seed and draw index

DO NOT silently narrow an input range after viewing results.
Any human edit creates assumptions_version + 1.
```

### Assumption-file schema

```json
{
  "experiment": "PV-to-NMES computational feasibility screen",
  "seed": 20260718,
  "draws": 50000,
  "assumptions_version": 1,
  "distribution": "triangular",
  "scenarios": {},
  "pv_chain": {},
  "protocols": {},
  "nmes_device": {},
  "screening_thresholds": {
    "energy_margin": 1.20,
    "preliminary_support_probability": 0.95
  },
  "human_approved": false,
  "approval_timestamp_utc": null
}
```

### Automated actions

```text
PROCEDURE PHASE_1_ASSUMPTION_LOCK:
    CALL INSPECT_ENVIRONMENT
    BUILD assumptions.json from the tables above
    VALIDATE units, ordering low <= mode <= high, fractions, and scenario IDs
    PRINT a compact assumption matrix and explicit "NOT MEASURED" warning
    WAIT for H1
    IF human approves:
        SET human_approved = true
        RECORD approval timestamp
        WRITE immutable approved copy into run directory
    ELSE:
        APPLY only explicit human edits
        INCREMENT assumptions_version
        VALIDATE again
```

### END condition

- Environment is recorded.
- Every variable has a unit and uncertainty range.
- `assumptions.json` is valid and human-approved.

### HUMAN_DECISION_REQUIRED H1

The human approves the illustrative defaults, edits specific values, removes an unjustified scenario, or stops. Approval means “acceptable for exploratory simulation,” not “scientifically verified.”

---

## Rapid Phase 2 — Build, test, and execute

### START condition

- H1 = approved.
- `assumptions.json` is locked and records human approval.

### Required equations

For each draw:

$$
E_{harvest,Wh}=G\,A\,\eta_{PV}\,F_{geometry}\,F_{transmission}\,\eta_{MPPT}\,\eta_{storage}\,t_{charge}
$$

Required stimulator voltage:

$$
V_{required}=I_{commanded}\,R_{electrode}
$$

Pulse-time fraction while a train is on:

$$
F_{pulse}=\min\left(1, n_{phases}\,PW\,f\right)
$$

Train duty factor:

$$
F_{train}=\frac{t_{on}}{t_{on}+t_{off}}
$$

Approximate average electrode power across simultaneous channels:

$$
P_{electrode}=n_{channels}\,I_{commanded}^{2}\,R_{electrode}\,F_{pulse}\,F_{train}
$$

Estimated total system power while a session is running:

$$
P_{system}=\frac{P_{electrode}}{\eta_{output}}+P_{overhead}
$$

Daily system energy:

$$
E_{system,Wh}=P_{system}\left(\frac{minutes_{session}}{60}\right)n_{sessions}
$$

Energy autonomy:

$$
EAR=\frac{E_{harvest,Wh}}{E_{system,Wh}}
$$

Joint screening success:

```text
joint_success = (EAR >= 1.20) AND (V_required <= V_compliance)
```

The electrical-load model is deliberately simplified. It estimates energy demand; it does not estimate human contraction or therapeutic dose.

### Unit and logic tests required before the full run

```text
TEST T01: zero irradiance returns zero harvested energy.
TEST T02: doubling area doubles harvested energy when other inputs are fixed.
TEST T03: doubling charging duration doubles harvested energy.
TEST T04: harvested energy never exceeds incident energy on exposed area.
TEST T05: all efficiencies remain in [0, 1].
TEST T06: EAR is finite and non-negative for valid positive demand.
TEST T07: required voltage equals current × impedance.
TEST T08: a deliberately excessive current-impedance pair is compliance-limited.
TEST T09: same seed and assumptions reproduce identical summary values.
TEST T10: different seed changes raw samples but not schema.
TEST T11: summary percentiles are ordered p05 <= median <= p95.
TEST T12: raw row count = draws × scenarios × protocols.
TEST T13: every CSV column has an explicit unit or is dimensionless.
TEST T14: no human-efficacy or safety conclusion appears in generated report templates.
TEST T15: minimum usable storage equals 1.20 × modeled daily system energy.
```

### Execution pseudocode

```text
PROCEDURE PHASE_2_BUILD_AND_EXECUTE(rerun=false):
    READ approved assumptions.json
    IF assumptions.human_approved != true:
        FAIL("Unapproved assumptions")

    WRITE run_experiment.py using Python standard library:
        modules = [json, csv, math, random, statistics, pathlib, hashlib, datetime]
    WRITE test_experiment.py

    RUN unit tests
    IF any required test fails:
        WRITE failure to run.log
        SET status = "FAILED_TESTS"
        DO NOT run Monte Carlo
        GO TO H2 with only [RERUN_AFTER_FIX, STOP_AS_FAILED]

    SET N = assumptions.draws
    IF remaining_time_minutes < 8:
        SET N = 10000
        RECORD deviation and reason

    INITIALIZE deterministic random generator with recorded seed

    FOR scenario IN scenarios:
        FOR protocol IN protocols:
            FOR draw_index IN 1..N:
                SAMPLE approved inputs
                CALCULATE E_harvest_Wh
                CALCULATE V_required and compliance_ok
                CALCULATE pulse_fraction and train_duty
                CALCULATE P_electrode and P_system
                CALCULATE E_system_Wh and EAR
                CALCULATE pv_fraction = min(1, E_harvest_Wh / E_system_Wh)
                CALCULATE minimum_usable_storage_Wh = 1.20 * E_system_Wh
                CALCULATE joint_success = (EAR >= 1.20) AND compliance_ok
                WRITE one raw_results.csv row

            CALCULATE p05, median, p95 for EAR, harvested Wh, and system Wh
            CALCULATE P(EAR >= 1.00)
            CALCULATE P(EAR >= 1.20 AND compliance_ok)
            CALCULATE P(compliance_ok)
            CALCULATE median PV fraction
            CALCULATE median minimum usable storage Wh
            WRITE scenario_summary.csv row

    WRITE summary.json
    RUN unit tests again against produced artifacts
    RECORD runtime, row counts, seed, assumptions hash, and code hash in run.log
    SET status = "EXECUTED_AWAITING_H2"
```

### END condition

- Required tests pass.
- Raw and summarized outputs exist.
- Seed, assumptions, code hashes, runtime, and deviations are logged.
- No interpretation beyond numeric summaries has been made.

### HUMAN_DECISION_REQUIRED H2

The human accepts the run as valid, authorizes one rerun with a new recorded seed, or stops and marks it failed. A rerun must never replace the first run; it receives a new subdirectory or explicit rerun ID.

---

## Rapid Phase 3 — Stress test and interpretation

### START condition

- H2 = ACCEPT.
- Tests and provenance checks passed.

### Automated stress tests

```text
PROCEDURE PHASE_3_STRESS_TEST_AND_INTERPRET:
    FOR each scenario × protocol:
        COMPUTE break_even_area at median values
        COMPUTE break_even_charge_hours at median values
        COMPUTE probability EAR >= 1.00
        COMPUTE probability EAR >= 1.20 AND compliance_ok
        COMPUTE probability compliance_ok

        FOR each uncertain input:
            COMPUTE Pearson correlation(input, log10(max(EAR, epsilon)))
        RANK inputs by absolute correlation
        WRITE top drivers to sensitivity.csv

    RUN boundary cases:
        B01 = all low values
        B02 = all mode values
        B03 = all high values
        B04 = zero-light interruption
        B05 = highest impedance + highest current + lowest compliance voltage
        B06 = highest electronics overhead

    CHECK whether any favorable EAR result is dominated by voltage non-compliance
    CHECK whether a conclusion reverses between median and 5th-percentile EAR
    CHECK whether result depends on one unsupported assumption
    WRITE numeric findings without causal or medical language
```

### Screening interpretation rules

These labels are internal rapid-screen categories, not technology-readiness or safety classifications.

| Numeric result | Allowed rapid-screen label |
|---|---|
| $P(EAR\ge1.20 \land compliance)\ge0.95$ and no failed validity check | **PRELIMINARY ENERGY SUPPORT under declared assumptions** |
| Probability from 0.50 to <0.95 | **CONDITIONAL / assumption-sensitive** |
| Probability <0.50 but median PV fraction ≥0.10 | **PV-ASSISTED only** |
| Probability <0.50 and median PV fraction <0.10 | **ENERGY-AUTONOMY NOT SUPPORTED** |
| Test, provenance, unit, or model-integrity problem | **INCONCLUSIVE / INVALID RUN** |

The agent recommends a label but the human selects the final interpretation at H3. The human may choose a more conservative label, never a stronger label than the numeric rule permits.

### Standard claim templates

```text
PRELIMINARY ENERGY SUPPORT:
"In this computer-only Monte Carlo screen, [SCENARIO] supplied at least a
1.20 modeled energy ratio while remaining within assumed voltage compliance
in [PERCENT]% of draws for [PROTOCOL]. This supports energy plausibility under
the declared assumptions, not physiological efficacy or hardware readiness."

CONDITIONAL:
"Modeled feasibility for [SCENARIO] was sensitive to [TOP VARIABLES]. Physical
measurement of these variables is required before an autonomy claim."

PV-ASSISTED:
"Harvested light supplied a non-trivial fraction of modeled demand but did not
meet the rapid experiment's robustness rule. The defensible framing is
PV-assisted or hybrid."

NOT SUPPORTED:
"The declared scenario did not support photovoltaic energy autonomy for the
candidate protocol in this model."

INCONCLUSIVE:
"The run cannot support an energy conclusion because [VALIDITY REASON]."
```

### END condition

- Sensitivity and boundary analyses exist.
- Every scenario-protocol result has a maximum permitted claim category.
- Limitations and reversals are visible.

### HUMAN_DECISION_REQUIRED H3

The human selects the allowed interpretation for each scenario, chooses a more conservative label, or marks the run inconclusive. Numeric files remain immutable.

---

## Rapid Phase 4 — Reproducible report

### START condition

- H3 decisions are recorded.

### Report-generation pseudocode

```text
PROCEDURE PHASE_4_REPORT:
    GENERATE report.md with these exact sections:
        1. Executive result
        2. Computer-only scope and prohibited claims
        3. Research question and hypotheses
        4. Human decisions H0-H3
        5. Environment and software versions
        6. Approved assumptions with units and status
        7. Equations and computational method
        8. Test results and deviations
        9. Scenario × protocol result matrix
        10. Sensitivity ranking
        11. Boundary and break-even cases
        12. Human-approved interpretation
        13. Limitations
        14. Required next physical measurement
        15. Artifact manifest

    REQUIRE report to include:
        seed, N, assumptions hash, code hash, run ID, start/end UTC
        p05/median/p95, not only best case
        compliance probability
        explicit statement "no human or hardware evidence"
        exact H3 wording

    IF matplotlib already installed AND remaining_time_minutes >= 3:
        CREATE optional EAR distribution and sensitivity plots
    ELSE:
        RECORD "plots skipped; tabular results are authoritative"

    SCAN report for prohibited phrases:
        ["proves muscle preservation", "safe for astronauts", "flight ready",
         "replaces exercise", "clinically effective"]
    FAIL report generation if a prohibited phrase is asserted rather than negated

    CREATE SHA256SUMS.txt for all final artifacts except the hash file itself
    SET status = "REPORTED_AWAITING_H4"
```

### END condition

- `report.md` can be read without the code.
- The result matrix includes uncertainty and voltage compliance.
- Limitations are adjacent to conclusions.
- Artifact hashes exist.

### HUMAN_DECISION_REQUIRED H4

The human approves wording, requests one auditable correction, or rejects the report. A wording correction may not change raw or summary numbers.

---

## Rapid Phase 5 — Close and handoff

### START condition

- H4 is recorded.

### Automated close procedure

```text
PROCEDURE PHASE_5_CLOSE:
    VERIFY every expected artifact or mark it MISSING with reason
    VERIFY hashes for immutable artifacts
    APPEND H4 decision and final status to README.md and run.log
    PRINT concise handoff:
        run path
        status
        strongest permitted energy conclusion
        weakest/failed scenario
        top three sensitivity drivers
        next physical measurement required
        total runtime
    DO NOT delete intermediate evidence
    DO NOT silently promote this run to baseline
    WAIT for H5
```

### END condition

- Run has status `BASELINE`, `EXPLORATORY`, `REJECTED`, or `FAILED`.
- Final human decision is recorded.
- The directory is reproducible and self-describing.

### HUMAN_DECISION_REQUIRED H5

The human chooses whether the run becomes the computational baseline, remains exploratory, or is marked failed.

---

## Rapid experiment success criteria

The 30-minute experiment itself is successful when:

1. it finishes with reproducible artifacts and passed validity tests;
2. assumptions are explicit and human-approved;
3. uncertainty and voltage compliance are included;
4. at least one energy claim is narrowed, supported conditionally, or rejected using prespecified rules;
5. no human-efficacy, medical-safety, or flight-readiness claim is made; and
6. the next physical measurement is identified.

A result showing that every scenario fails can still be a successful experiment. A favorable number without provenance, uncertainty, or claim discipline is a failed experiment.

## Minimum next measurement selected by the computer experiment

After ranking sensitivity, the report must recommend **one** next physical measurement:

```text
IF electronics_overhead is top driver:
    next_measurement = "Measure real stimulator + sensor Wh for one candidate session"
ELSE IF irradiance or transmission is top driver:
    next_measurement = "Log plane-of-array irradiance in the intended charging location"
ELSE IF exposed_area or geometry is top driver:
    next_measurement = "Measure effective illuminated area during wear and deployed charging"
ELSE IF impedance/current/compliance dominates:
    next_measurement = "Bench-test a certified stimulator into safe electronic loads; no human"
ELSE:
    next_measurement = "Validate the highest-ranked uncertain input with calibrated hardware"
```

---

## Proposed post-position-paper research agenda

The sections below define the later hardware, human-factors, unloading-analog, and relevant-environment programme proposed by the position paper. They do not occur within the 30-minute computer-only probe, and they are not reported as completed studies.

## Future validation programme abstract

Long-duration spaceflight and planetary habitation expose crew to mechanical unloading, while the equipment, power, time, and maintenance capacity available for exercise countermeasures remain constrained. The future validation programme would investigate a garment that harvests intermittent light through photovoltaic surfaces, buffers the energy in isolated storage, and allocates it to controlled neuromuscular electrical stimulation (NMES) of lower-limb antigravity muscles. Its intended role is narrow but consequential: to maintain a limited muscle-care capability during temporary interruptions to normal resistive and aerobic exercise caused by equipment failure, maintenance, power rationing, injury-related restriction, scheduling conflict, or operational emergency. The garment is therefore framed as a **contingency bridge**, not an exercise replacement.

The research separates three claims that require different evidence: (1) NMES attenuates selected indices of disuse-related muscle deterioration during a defined exercise interruption; (2) a photovoltaic garment can collect enough usable energy, under explicitly stated illumination conditions, to deliver a meaningful fraction of the prescribed stimulation dose; and (3) adaptive control can allocate that dose without unacceptable pain, fatigue, skin injury, loss of user agency, or interference with crew operations. A staged mixed-method programme is proposed: requirements and hazard analysis; benchtop energy and durability validation; acute closed-loop NMES testing; habitat-analog operational evaluation; a randomized assessor-blinded 6° head-down-tilt bed-rest study; and, only after predefined gates are met, relevant-environment integration. The central physiological endpoint is change in lower-limb muscle volume. Engineering, safety, operational, and human-factors outcomes are treated as equally necessary gates rather than decorative secondary measures.

---

## 1. Research position

### 1.1 One-sentence thesis

> A photovoltaic NMES garment may preserve a bounded, user-controlled muscle-maintenance capability during short interruptions to centralized exercise infrastructure, even when it cannot reproduce the full musculoskeletal, cardiovascular, sensorimotor, and metabolic benefits of exercise.

### 1.2 High-impact use case

The primary use case is a **contingency muscle-maintenance layer** during a temporary loss or restriction of normal exercise capacity.

Representative triggers include:

- failure or maintenance of centralized exercise hardware;
- temporary habitat power rationing;
- exercise-device scheduling conflicts;
- mission operations that displace normal training time;
- temporary restriction after injury, subject to medical authorization; and
- emergency periods in which compact, distributed redundancy has higher value than peak training performance.

The project does not claim that such a garment should replace a treadmill, cycle ergometer, resistive exercise device, rehabilitation, or medical care. NASA's evidence review identifies exercise as the established countermeasure for spaceflight deconditioning and notes an allocation of approximately 2.5 hours per day on the ISS when setup, stowage, and hygiene are included [1]. ESA's EasyMotion investigation has already demonstrated the feasibility of wearing an electro-muscle-stimulation suit during exercise on the ISS, but not a photovoltaic, autonomous, or contingency-only system [2]. Documented ARED cable fraying and the broader maintenance history of ISS exercise-system cables make temporary interruption a credible systems scenario rather than a purely fictional one [14,15].

### 1.3 What “photovoltaic” means here

“Photovoltaic” means conversion of light to electrical energy. It does **not** mean human photosynthesis. Photobiomodulation is also outside the core intervention because it has a different mechanism and would confound causal interpretation. If investigated later, photobiomodulation should be a separately powered, separately controlled factorial module.

### 1.4 Intended garment context

The first system is a **habitat or transit garment**, not an EVA pressure suit. Photovoltaic collection may occur:

1. while the garment is worn in an illuminated safe area;
2. while removable or fold-out photovoltaic panels are deployed at a charging location; or
3. through a hybrid mode in which harvested energy supplements, rather than replaces, habitat power.

Any claim concerning use outside a pressure vessel requires a separate environmental, thermal, dust, radiation, flammability, and suit-integration qualification programme.

---

## 2. Problem, gap, and novelty

### 2.1 Established knowledge

- Mechanical unloading can rapidly reduce lower-limb muscle size and function.
- Resistive and aerobic exercise remain the primary integrated countermeasures.
- NMES can induce muscle contraction and has attenuated muscle-thickness loss in short bed-rest studies, but preservation of muscle size does not guarantee preservation of maximal strength. In a 2024 five-day study, quadriceps NMES preserved muscle thickness while maximal voluntary contraction declined despite stimulation [3].
- NASA has investigated electromyostimulation for spaceflight muscle loss and emphasized that both delivered current and resultant force must be measured [4].
- Six-degree head-down-tilt bed rest is a well-established ground analog for selected effects of unloading, but it is not equivalent to spaceflight [5].
- Flexible and textile photovoltaics can harvest light, but laboratory demonstrations do not establish garment-level energy sufficiency, durability, cleanability, or space-habitat compatibility [6,7].

### 2.2 Research gap

No validated integrated system currently establishes the full causal chain:

```text
Intermittent local light
        ↓
measured usable electrical energy
        ↓
isolated storage and power conditioning
        ↓
verified stimulation waveform and evoked muscle force
        ↓
safe, tolerable physiological dose
        ↓
attenuation of deterioration during an exercise interruption
        ↓
operationally useful distributed health redundancy
```

Most prior work validates only one or two links. The novelty is not the independent existence of PV, batteries, NMES, or smart garments. It is the rigorous integration of **energy provenance, physiological dose, adaptive safety, operational interruption, and user agency** into one falsifiable system claim.

### 2.3 Conceptual contribution: habitat resource metabolism

The garment is treated as a micro-scale resource loop within the resource metabolism of an off-world habitat:

```text
Local resource availability → harvest → store → allocate → maintain a human subsystem
```

This is a systems and Space-HCI proposition, not a claim that garment photovoltaics outperform central generation. Light is used as a difficult design case for handling an intermittent local resource. Lunar shadow, low solar angles, dust, and Martian atmospheric dust can all reduce collection; therefore, availability must be measured rather than assumed [8,9].

---

## 3. Aim, objectives, research questions, and hypotheses

### 3.1 Overall aim

To determine whether a photovoltaic, energy-aware NMES garment can provide a safe and operationally useful bridge for lower-limb muscle maintenance during a defined interruption to normal exercise in an off-world habitat scenario.

### 3.2 Objectives

1. Quantify the garment's usable energy yield across declared illumination, orientation, deformation, contamination, and charging scenarios.
2. Establish a reproducible relationship among electrical waveform, electrode interface, evoked force, discomfort, fatigue, and energy consumption.
3. Develop and verify a constrained closed-loop controller that adapts dose only within clinician-approved limits.
4. Evaluate user comprehension, consent, override, trust calibration, and task interference.
5. Test whether active NMES attenuates lower-limb muscle-volume loss during a controlled unloading period.
6. Determine whether an energy-budgeted protocol can preserve a prespecified fraction of the physiological dose delivered by an unconstrained reference protocol.
7. Produce evidence-based go/no-go criteria for further habitat-analog or spaceflight development.

### 3.3 Research questions

**RQ1 — Physiological efficacy:** During a defined exercise interruption under unloading, does active garment-delivered NMES attenuate loss of quadriceps muscle volume relative to sham stimulation?

**RQ2 — Energy feasibility:** Under each explicitly declared light-exposure scenario, what fraction of prescribed NMES energy can garment-integrated PV supply after conversion, storage, and control losses?

**RQ3 — Dose equivalence:** Can a resource-aware controller maintain a clinically and operationally meaningful evoked-force dose under intermittent energy constraints compared with a grid-unconstrained NMES reference?

**RQ4 — Safety:** Can stimulation be delivered without serious device-related adverse events and within predefined limits for pain, skin response, muscle damage, thermal rise, unintended movement, and electrical faults?

**RQ5 — Human agency and operational fit:** Can users understand system state, energy availability, target muscle, reason for stimulation, and expected duration—and stop the system immediately—without unacceptable workload or interference?

**RQ6 — Resilience value:** How many scheduled muscle-maintenance sessions remain deliverable during simulated failure of central exercise infrastructure and central power access?

### 3.4 Hypotheses

**H1:** Participants receiving active NMES during 14 days of 6° head-down-tilt bed rest will show a smaller percentage reduction in quadriceps muscle volume than participants receiving sham stimulation.

**H2:** Active NMES will not necessarily preserve maximal voluntary strength to the same degree as muscle volume; strength is therefore a key secondary endpoint, not evidence of exercise equivalence.

**H3:** A resource-aware controller will deliver a greater normalized torque-time integral per watt-hour than a fixed-parameter controller while remaining within identical stimulation and comfort limits.

**H4:** In at least one prespecified charging scenario, stored PV energy will supply the full energy required for the contingency protocol with a positive engineering reserve. This hypothesis must be tested separately for every claimed lunar, Martian, transit, or indoor-light scenario.

**H5:** Explicit previews, reason displays, countdowns, and a hardware stop control will improve state comprehension and perceived control relative to a minimally explained interface without increasing task completion time.

### 3.5 Non-claims

The project will not claim that:

- NMES replaces resistive or aerobic exercise;
- preservation of muscle thickness alone means preservation of strength or function;
- PV is sufficient at all off-world sites or times;
- an Earth solar-simulator result demonstrates lunar or Martian field performance;
- an energy-neutral day implies long-term reliability;
- “AI” can independently prescribe stimulation;
- PBM and NMES are the same intervention; or
- a habitat garment is ready for EVA use.

---

## 4. Conceptual and operational framework

### 4.1 Causal model

| Layer | Input | Mechanism | Output | Principal confounders or moderators |
|---|---|---|---|---|
| Environment | Irradiance, spectrum, angle, duration | Photovoltaic conversion | Raw DC energy | Dust, shadow, temperature, bending, shading by body |
| Power system | Raw DC energy | MPPT, storage, conversion, isolation | Usable regulated energy | Conversion loss, battery age, thermal limits |
| Controller | Energy state, session prescription, sensors | Constrained scheduling and waveform selection | Commanded NMES dose | Forecast error, sensor error, software fault |
| Electrode interface | Commanded waveform | Transcutaneous current delivery | Measured current and voltage | Placement, sweat, impedance, lift, skin condition |
| Neuromuscular system | Delivered waveform | Motor-unit recruitment and contraction | Evoked force/torque | Anatomy, fatigue, tolerance, prior training, hydration |
| Physiological outcome | Repeated evoked-force dose | Muscle activation during unloading | Muscle size/function change | Diet, protein, sleep, baseline fitness, systemic effects |
| Human-system outcome | Information and control | Understanding, consent, override | Safe adoption and calibrated trust | Workload, discomfort, alarm burden, privacy |
| Habitat outcome | Distributed stored energy | Continuity during outage | Sessions retained | Duration of outage, charging opportunity, competing loads |

### 4.2 Operational definitions

| Construct | Operational definition |
|---|---|
| **Exercise interruption** | A prespecified period in which the normal resistive/aerobic countermeasure is unavailable or medically restricted. The principal efficacy study models 14 days; results must not be extrapolated to longer outages without evidence. |
| **Safety net** | A secondary, bounded capability intended to reduce the physiological cost of an interruption until primary exercise resumes. |
| **Delivered electrical dose** | Measured per-channel current, voltage, pulse width, frequency, pulse count, train duration, duty cycle, and accumulated charge; commanded values alone are insufficient. |
| **Physiological dose** | Evoked torque-time integral normalized to the participant's baseline maximal voluntary contraction (MVC), reported by muscle group and session. |
| **Useful harvested energy** | Energy entering protected storage after PV and maximum-power-point-tracking losses, not nameplate PV output. |
| **Energy autonomy ratio, EAR** | Useful harvested energy divided by total energy consumed by stimulation, sensing, control, communication, storage, and conversion during the same accounting window. |
| **Continuity ratio** | Completed eligible contingency sessions divided by scheduled eligible sessions during simulated central-infrastructure unavailability. |
| **User agency** | Correct state comprehension, informed session initiation, ability to pause/stop, and post-session understanding of what was delivered and why. |
| **Acceptability** | Multidimensional assessment of discomfort, burden, movement restriction, thermal comfort, don/doff effort, hygiene, privacy, and willingness to reuse. |

### 4.3 Core equations

Usable harvested energy over interval $T$:

$$
E_{harvest}=\int_T G(t)\,A_{exposed}(t)\,\eta_{PV}(t)\,\eta_{MPPT}(t)\,\eta_{store}(t)\,dt
$$

Total system energy for the same accounting interval:

$$
E_{system}=\int_T\left(P_{stim}+P_{sense}+P_{compute}+P_{interface}+P_{communications}+P_{loss}\right)dt
$$

Energy autonomy ratio:

$$
EAR=\frac{E_{harvest}}{E_{system}}
$$

Normalized physiological dose for a muscle group:

$$
D_{phys}=\frac{1}{MVC_{baseline}}\sum_{k=1}^{n}\int_{train_k}\tau_{evoked}(t)\,dt
$$

The project should report all three quantities. Electrical energy is not a valid proxy for physiological dose when electrode contact, fatigue, and individual recruitment differ.

---

## 5. System under investigation

### 5.1 Functional architecture

```text
PV textile / removable PV panel
              ↓
  MPPT + protected charge controller
              ↓
 isolated energy storage + fuel gauge
              ↓
 medical-grade isolated NMES power stage
              ↓
  independently limited output channels
              ↓
 mapped textile electrodes on lower-limb muscles

Sensors → safety state machine → bounded controller → user preview/consent
                         ↑                         ↓
             hardware watchdog             hardware STOP
```

The photovoltaic source must never be connected directly to the body electrodes. Stimulation is supplied from protected storage through an isolated, current-controlled, charge-balanced output stage.

### 5.2 Initial muscle scope

The first human studies should use modular lower-limb channels rather than simultaneous whole-body stimulation:

- quadriceps;
- plantar flexors; and
- optionally hamstrings or gluteals after separate acute safety calibration.

Muscle groups should be stimulated sequentially unless a medical and electrical safety review explicitly approves otherwise. The torso, head, anterior neck, and current paths across the chest are outside the proposed scope.

### 5.3 Sensor set

Minimum sensors and signals are:

- electrode-skin impedance or equivalent contact-quality measurement;
- measured stimulation current and voltage at the output stage;
- skin-adjacent and electronics temperature;
- limb motion and posture from inertial sensors;
- evoked torque, force, or mechanomyography during calibration and validation;
- storage state of charge, state of health, voltage, current, and temperature;
- harvested power and energy at the PV and storage boundaries; and
- physical stop, pause, fault, and user-confirmation events.

Surface EMG may be useful between trains but should not be treated as a clean control signal during stimulation unless artifact rejection is independently validated.

### 5.4 Safety state machine

```text
OFF
 ↓ user request
SELF-CHECK ──fault──→ LOCKOUT
 ↓ pass
SKIN / CONTACT CHECK ──fail──→ REPOSITION
 ↓ pass
CALIBRATION ──pain, motion, limit──→ STOP
 ↓ clinician-approved envelope stored
PREVIEW + USER CONFIRMATION
 ↓
ARMED
 ↓ safe posture confirmed
STIMULATE ↔ REST
  │  ↑
  │  └── adaptive changes only inside approved envelope
  ├── user pause/stop → SAFE OFF
  ├── posture/contact/temperature fault → SAFE OFF
  └── watchdog/power fault → FAIL OPEN / SAFE OFF
```

There is no autonomous background start. Every session requires a preview and affirmative initiation by the wearer or authorized clinician. Emergency stop must be physical, immediately reachable, and independent of the display, consistent with human-rated interface principles in NASA-STD-3001 Volume 2 [10].

### 5.5 Control objective

The controller is not a diagnostic or prescribing agent. It solves a bounded allocation problem:

> Deliver the prescribed normalized torque-time integral, within clinician-approved waveform, comfort, fatigue, posture, contact, thermal, and energy constraints, while preserving a declared reserve.

Rules that can increase stimulation amplitude, pulse width, or duty cycle require conservative hard limits in hardware and firmware. A learned model may forecast fatigue or energy availability, but it cannot override those limits, initiate treatment, or silently change the clinical target.

---

## 6. Methodological overview

### 6.1 Research design

The programme uses **sequential mixed methods with engineering and clinical stage gates**. Physiological efficacy is not tested with an unverified power stage, and integrated flight claims are not made from benchtop or analog evidence.

| Work package | Main question | Method | Primary output | Gate |
|---|---|---|---|---|
| WP0 | What must the system do, and what can harm the user? | Scenario analysis, co-design, STPA/FMEA, requirements traceability | Intended-use statement and hazard-controlled requirements | G0 |
| WP1 | Can the garment harvest, store, and replay sufficient energy? | Benchtop factorial testing and hardware-in-the-loop load replay | Scenario-specific EAR and durability | G1 |
| WP2 | Can the device deliver a stable, tolerable physiological dose? | Randomized acute crossover study | Torque-time integral per Wh, safety, comfort | G2 |
| WP3 | Does it fit real operational routines and outage scenarios? | Habitat-analog deployment and mixed methods | Continuity, task interference, agency | G3 |
| WP4 | Does it attenuate muscle deterioration during unloading? | Randomized assessor-blinded 6° HDT bed-rest study | Change in quadriceps muscle volume | G4 |
| WP5 | Does the integrated system remain safe in a relevant environment? | Environmental qualification, parabolic/space pilot as approved | Integrated performance and fault evidence | G5 |

### 6.2 Evidence hierarchy

Claims must be limited to the environment and outcome actually tested:

1. component performance;
2. integrated benchtop performance;
3. acute human safety and dose control;
4. operational feasibility in an analog;
5. physiological effect in a controlled unloading analog;
6. relevant-environment performance; and
7. flight performance.

This ordering follows the logic of NASA's Technology Readiness Levels; it does not itself assign an official TRL [11].

---

## 7. WP0 — Requirements, co-design, and hazard analysis

### 7.1 Participants

Purposive sampling should include:

- aerospace medicine and rehabilitation clinicians;
- NMES researchers or physiotherapists;
- spacecraft power and battery engineers;
- textile and pressure-garment engineers;
- human-factors and Space-HCI researchers;
- mission planners or astronaut-analog crew; and
- medical-device safety and regulatory specialists.

Target qualitative sample size should be governed by information power and stakeholder coverage, not a ritual fixed number. An initial target of 15–25 expert sessions plus two multidisciplinary workshops is reasonable.

### 7.2 Procedure

1. Define intended users, use environment, excluded uses, outage duration, and fallback power mode.
2. Conduct critical-incident interviews concerning exercise interruption, discomfort, false alarms, power scarcity, privacy, and emergency override.
3. Map task sequences: donning, electrode alignment, self-check, calibration, session preview, stimulation, pause, stop, doffing, cleaning, charging, maintenance, and fault recovery.
4. Conduct System-Theoretic Process Analysis (STPA) and Failure Modes and Effects Analysis (FMEA).
5. Convert findings into traceable system and study requirements.
6. Test low-fidelity interface concepts for state comprehension and emergency stop.

### 7.3 Minimum hazard set

- unintended contraction during locomotion or precision work;
- fall, collision, loss of hand control, or interference with emergency response;
- stimulation across unsafe anatomical paths;
- excessive current, pulse charge, duty cycle, or session accumulation;
- electrode lift, high local current density, skin injury, sweat-related contact change;
- muscle overuse, extreme creatine-kinase elevation, or rhabdomyolysis;
- battery thermal event, overcharge, short circuit, or conductive sweat ingress;
- PV overvoltage or unsafe charging state;
- incorrect garment size or electrode placement;
- sensor or algorithm error interpreted as permission to increase dose;
- loss of communications or corrupt configuration;
- unauthorized remote initiation;
- user inability to understand, pause, or stop the system;
- hygiene failure and cross-contamination; and
- overreliance that delays restoration of normal exercise or medical evaluation.

### 7.4 Gate G0

Proceed only when intended use and exclusions are fixed, safety-critical requirements are traceable to hazards, independent hardware limits are specified, and the garment has a physical stop independent of its screen or network.

---

## 8. WP1 — Photovoltaic, storage, and durability validation

### 8.1 Study design

Use a repeated-measures factorial benchtop design with at least three independently fabricated garment or panel specimens per configuration. Report specimen-level data; repeated readings from one specimen are not independent replicates.

### 8.2 Test factors

#### Illumination

- calibrated terrestrial solar-simulator baseline;
- mission-specific spectral and irradiance profiles where defensible;
- low-angle incidence relevant to lunar polar concepts;
- habitat/window-filtered light;
- representative artificial habitat lighting;
- intermittent shadow sequences; and
- Mars clear-sky and dust-attenuated scenarios.

Every profile must state spectrum, plane-of-array irradiance, angle, duration, temperature, and uncertainty. “Sunlight” is not a sufficient methods description.

#### Garment state

- flat reference;
- worn on a thermal/manikin form;
- bent at specified radii;
- locally wrinkled;
- partially shaded by limbs or equipment; and
- deployed in a removable or fold-out charging configuration.

#### Degradation and contamination

- repeated flexion and don/doff cycles;
- sweat and humidity exposure;
- approved cleaning cycles;
- abrasion;
- connector cycling;
- relevant dust simulant on external charging surfaces; and
- thermal cycling appropriate to the declared habitat location.

Vacuum, radiation, atomic oxygen, and extreme thermal testing are required only for components claimed to operate outside the habitat, but those claims cannot proceed without such testing.

### 8.3 Instrumentation and calibration

- calibrated reference cell or spectroradiometer;
- four-wire electrical measurement where applicable;
- maximum-power-point tracker telemetry;
- coulomb counting at storage input and output;
- programmable electronic load replaying measured NMES demand;
- thermocouples or RTDs on PV, storage, power electronics, and skin-facing surfaces; and
- synchronized logging with calibration certificates and uncertainty budgets.

### 8.4 Outcomes

**Primary engineering outcome:** EAR for each complete, declared light-and-use scenario.

Secondary outcomes:

- Wh/day entering protected storage;
- peak and median power at the PV, MPPT, storage, and load boundaries;
- round-trip storage efficiency;
- stimulation-session energy including all auxiliary loads;
- fraction of scheduled sessions deliverable;
- time to accumulate one session's energy;
- degradation after bend, sweat, cleaning, abrasion, dust, and thermal tests;
- areal and mass-specific useful energy yield;
- temperature rise; and
- number and type of protection or controller faults.

### 8.5 Hardware-in-the-loop energy provenance

The power study should distinguish three modes:

1. **Physical PV mode:** the session uses energy actually harvested and stored by the prototype.
2. **PV-budget emulation:** a certified laboratory power system delivers stimulation while software enforces an energy budget derived from measured PV profiles.
3. **Hybrid fallback mode:** central power is explicitly allowed and its contribution is separately metered.

Energy origin must be logged. A battery precharged from the grid cannot be reported as a solar-powered session.

### 8.6 Proposed Gate G1

For any scenario advertised as “energy autonomous,” the prespecified test campaign should demonstrate:

- median $EAR \ge 1.20$, providing an engineering reserve;
- lower-tail performance sufficient for the agreed continuity target;
- no unsafe thermal or protection event;
- delivery of the full verified load profile from protected storage; and
- degradation within a prospectively declared service-life limit.

If these conditions are not met, the system must be described as **PV-assisted** or **hybrid**, not autonomous. Failure of G1 does not invalidate the NMES hypothesis; it falsifies the energy-autonomy claim.

---

## 9. WP2 — Acute closed-loop NMES study

### 9.1 Purpose

To establish individual calibration, waveform delivery accuracy, evoked-force control, energy efficiency, discomfort, fatigue, and immediate safety before any unloading efficacy trial.

### 9.2 Design

Randomized, counterbalanced, within-participant crossover with washout sufficient for evoked force and perceived fatigue to return to the prespecified baseline range.

Candidate conditions:

1. fixed-parameter NMES;
2. constrained adaptive NMES with unconstrained energy availability; and
3. constrained adaptive NMES under replayed intermittent PV budgets.

The controller can be compared fairly only when all conditions share identical hard safety limits and physiological targets.

### 9.3 Participants

Healthy adults broadly representative of the intended crew anthropometry and sex distribution. A target of approximately 24–30 completers is suitable for an acute estimation study, but the final sample must follow a within-participant power analysis based on the smallest relevant difference in normalized torque-time integral per Wh.

Exclusion criteria must be finalized by the study physician and ethics board. They should address implanted electronic devices, relevant cardiac or neurological disease, seizure risk, pregnancy, impaired sensation, active skin disease at electrode sites, recent surgery or injury, vascular risk, current illness, and any condition that makes forceful involuntary contraction unsafe.

### 9.4 Positioning and task restriction

Initial testing occurs seated or supine with the tested limb supported and instrumented. No stimulation occurs during standing, walking, vehicle control, emergency procedure, tool use, or other operational task.

### 9.5 Calibration

1. Inspect and document skin.
2. Align electrodes using anatomical landmarks and a placement template.
3. Measure contact quality.
4. Measure baseline MVC with standardized dynamometry.
5. Increase stimulation gradually within the approved envelope to identify motor threshold, tolerable working level, and evoked torque.
6. Record actual current, voltage, waveform, contact state, discomfort, and force.
7. Store participant-specific limits with version control.

A literature-anchored starting candidate is a charge-balanced biphasic waveform with a short low-frequency warm-up followed by tetanic stimulation. Hansen et al. used a 6 Hz, 300 μs warm-up followed by 60 Hz, 400 μs biphasic stimulation with 5-second contractions and 10-second rests [3]. These parameters are a starting reference, **not a garment prescription**. WP2 must determine the lowest tolerable dose that reaches the predefined evoked-force target with the certified research stimulator.

### 9.6 Primary outcomes

- normalized torque-time integral per Wh; and
- between-condition difference in achieved physiological dose relative to the prescribed target.

### 9.7 Secondary outcomes

- within-session torque decline and recovery;
- waveform accuracy and output-limit events;
- electrode impedance and lift events;
- Borg CR10 discomfort and fatigue ratings;
- skin response immediately, 30 minutes, and 24 hours after stimulation;
- device and skin-adjacent temperature;
- unintended limb displacement;
- user stop latency and stop success;
- perceived control, trust calibration, and willingness to repeat; and
- adverse events.

### 9.8 Gate G2

Proceed only if the integrated garment can reproducibly deliver the target physiological dose, the hardware stop terminates output within the verified requirement, contact or posture faults fail safe, and no unresolved serious device-related adverse event occurs. Feasibility thresholds for discomfort, skin response, and dose completion must be declared before enrollment.

---

## 10. WP3 — Habitat-analog operational study

### 10.1 Purpose

To test whether the garment behaves as a useful contingency system in daily routines, rather than only as a laboratory stimulator.

### 10.2 Design

A 7–14-day habitat-analog deployment using repeated outage scenarios. This study is not powered to infer muscle preservation. It evaluates workflow, continuity, comprehension, resource allocation, hygiene, maintenance, and social acceptability.

Scenarios should include:

- exercise device unavailable for 24, 72, and 168 hours;
- PV collection reduced by shadow or dust profile;
- central power unavailable to the garment;
- one failed electrode channel;
- inaccurate energy forecast;
- schedule conflict requiring rescheduling; and
- a deliberate user cancellation.

Stimulation still occurs only in medically approved stationary windows. Operational tasks are simulated for interface evaluation with stimulation disabled unless a later safety protocol explicitly permits otherwise.

### 10.3 Mixed-method outcomes

#### Quantitative

- continuity ratio;
- eligible sessions accepted, postponed, cancelled, completed, or faulted;
- user comprehension of system state and reason;
- time to don, align, calibrate, start, stop, doff, and clean;
- NASA-TLX or equivalent workload;
- discomfort, thermal comfort, mobility restriction, and sleep interference;
- number of unnecessary alarms and alarm-response time;
- charging opportunities and measured EAR; and
- maintenance time and consumables.

#### Qualitative

- semi-structured interviews after normal and off-nominal scenarios;
- critical-incident logs;
- researcher observation of workarounds and misuse;
- explanation-quality interviews: “What is the system doing, why, and what happens if you stop it?”; and
- concerns about privacy, bodily autonomy, remote oversight, and dependence.

### 10.4 Analysis

Use descriptive estimates with uncertainty for feasibility outcomes. Conduct reflexive thematic analysis with an explicit coding process, negative-case analysis, and a mixed-method joint display linking logged events to participant accounts. Do not turn a small analog crew sample into an underpowered efficacy test.

### 10.5 Gate G3

Proceed when the device meets prospectively specified continuity and comprehension targets, users can stop every session without assistance, critical tasks remain protected from stimulation, and recurrent faults or workarounds have been resolved or formally accepted.

---

## 11. WP4 — Randomized 6° head-down-tilt bed-rest efficacy study

### 11.1 Design

Randomized, controlled, parallel-group, assessor-blinded superiority study with a nested engineering comparison.

Proposed arms:

- **Arm A — Sham control:** identical garment and workflow with credible sensory-level or brief ramp-down stimulation that does not produce the target contraction.
- **Arm B — Active reference NMES:** active, individually calibrated stimulation with energy unconstrained by the PV budget.
- **Arm C — PV-budgeted active NMES:** the same approved controller and target, but session timing and dose are constrained by prospectively measured PV-energy profiles.

All electrical stimulation should initially be delivered by a certified research stimulator or verified isolated medical-grade output stage. PV-budget emulation should be used if the experimental PV hardware has not yet passed all human-use safety tests. This protects participants and prevents a power-stage fault from obscuring the physiological question.

### 11.2 Population

Healthy adults who pass medical and psychological screening for strict head-down-tilt bed rest and NMES. Recruitment should target representation across sex and the intended adult anthropometric range. Eligibility and withdrawal criteria must match the analog facility's medical standard.

### 11.3 Sample size

The confirmatory sample must be calculated from:

1. the smallest worthwhile between-group difference in percentage quadriceps-volume change;
2. variance from a directly comparable pilot or blinded internal-pilot estimate;
3. the primary two-sided alpha and desired power;
4. expected attrition; and
5. multiplicity from the hierarchical testing sequence.

No universal effect size should be borrowed from an unrelated clinical population. If an initial planning number is required for budgeting, approximately 15–20 completers per arm may be used only as a provisional feasibility estimate, not as proof that the study is adequately powered.

### 11.4 Randomization and masking

- computer-generated permuted blocks of varying size;
- stratification by sex and baseline quadriceps muscle volume or MVC;
- allocation concealed until enrollment is complete;
- imaging, dynamometry, laboratory, and statistical assessors blinded to group;
- separate staff for intervention delivery and outcomes; and
- post-study assessment of participant treatment guess and expectancy.

Participants will often perceive active contraction, so full participant blinding is unlikely. This limitation must be acknowledged rather than hidden behind the word “double-blind.”

### 11.5 Exposure schedule

1. **Baseline and familiarization:** 3–7 days with controlled measurements, diet stabilization, device calibration, and no exhaustive lower-limb exercise near outcome testing.
2. **Strict 6° head-down-tilt bed rest:** 14 days under facility-standard controls.
3. **Recovery and safety follow-up:** facility-defined reambulation plus at least one delayed skin and adverse-event assessment.

The 6° model is appropriate for controlled countermeasure testing but reproduces only selected features of spaceflight [5]. Diet, energy intake, protein intake, hydration, sleep opportunity, medication, and permitted movement must be standardized or recorded.

### 11.6 Intervention dose

The final regimen must be selected from WP2 and specified by:

- target muscles and electrode locations;
- waveform shape and charge balance;
- measured amplitude and voltage compliance;
- pulse width and frequency;
- train duration, ramp, rest interval, and duty cycle;
- target normalized evoked torque;
- maximum daily accumulated dose;
- adaptation rules;
- missed-dose rules; and
- medical and device stop criteria.

Do not prescribe one fixed milliampere value to all participants. Current required for a target contraction depends on anatomy and the electrode-skin interface. Do not extrapolate a quadriceps-only regimen directly to simultaneous whole-body stimulation.

### 11.7 Outcomes and measurement schedule

#### Primary physiological outcome

Percentage change in quadriceps muscle volume from baseline to the end of bed rest, measured by blinded MRI segmentation using a preregistered acquisition and analysis protocol.

#### Key secondary physiological outcomes

- plantar-flexor and, if included, hamstring/gluteal muscle volume;
- ultrasound muscle thickness and architecture;
- isometric MVC and rate of force development;
- electrically evoked torque and fatigue profile;
- voluntary activation where feasible;
- functional mobility, balance, and locomotor outcomes after reambulation;
- lower-limb lean mass by DXA if available;
- biomarkers selected for safety or mechanism, including creatine kinase and renal indicators under medical oversight; and
- participant-reported soreness, pain, fatigue, and perceived readiness.

#### Engineering outcomes

- prescribed versus delivered electrical and physiological dose;
- Wh consumed by stimulation and by the total system;
- PV-origin Wh assigned and actually available;
- EAR and continuity ratio;
- contact-quality faults, thermal events, controller overrides, and missed trains; and
- energy cost per unit normalized torque-time integral.

#### Human-factors outcomes

- state and reason comprehension;
- discomfort and acceptability;
- trust calibration;
- stop-control performance;
- don/doff, alignment, cleaning, and maintenance time; and
- qualitative accounts of bodily agency and perceived coercion.

#### Suggested schedule

| Measure | Baseline | Early bed rest | Midpoint | End bed rest | Recovery |
|---|---:|---:|---:|---:|---:|
| MRI muscle volume | ✓ |  |  | ✓ | optional |
| Ultrasound | ✓ | ✓ | ✓ | ✓ | ✓ |
| MVC/RFD | ✓ | if facility permits |  | ✓ | ✓ |
| Calibration and evoked torque | ✓ | ✓ | ✓ | ✓ |  |
| Skin examination | ✓ | every session | every session | every session | ✓ |
| CK/renal safety panel | ✓ | after initial loading as approved | risk-triggered | ✓ | risk-triggered |
| Energy and waveform telemetry |  | continuous per session | continuous | continuous |  |
| Acceptability/workload | ✓ | ✓ | ✓ | ✓ | interview |

### 11.8 Primary contrasts and testing hierarchy

1. **Physiological superiority:** Arm B versus Arm A for percentage quadriceps-volume change.
2. **Resource-constrained effectiveness:** Arm C versus Arm A, tested only after the active reference demonstrates the expected direction and the hierarchy permits.
3. **Dose non-inferiority:** Arm C versus Arm B for achieved normalized torque-time integral, using a prospectively justified margin.
4. **Exploratory physiological comparison:** Arm C versus Arm B for muscle-volume and strength outcomes.

The non-inferiority margin must be defined from a clinically and operationally acceptable loss of dose before unblinding. It cannot be selected after seeing the data.

### 11.9 Statistical analysis

- preregister protocol, hypotheses, primary outcome, hierarchy, exclusions, and analysis code;
- analyze the primary superiority estimand under intention to treat;
- use a linear model or mixed-effects model with end-point change or repeated measurements, adjusting for baseline value and randomization strata;
- report adjusted mean differences, standardized effects where useful, 95% confidence intervals, and exact p-values;
- inspect distributional assumptions and use robust or transformed analyses when prespecified;
- report both intention-to-treat and per-protocol results for non-inferiority;
- distinguish missing sessions caused by the energy constraint, device failure, intolerance, and unrelated participant withdrawal;
- use sensitivity analyses for missing outcome data and transparent reasons for missingness;
- control multiplicity for confirmatory comparisons; and
- treat biomarker, subgroup, and mediation analyses as exploratory unless powered and preregistered.

Sex, baseline fitness, baseline muscle volume, adipose thickness at the electrode site, and tolerance may be examined as moderators, but small-sample subgroup claims should be avoided.

### 11.10 Gate G4

Advancement requires all of the following:

- a favorable, sufficiently precise active-versus-sham estimate for the primary outcome;
- no unresolved serious device-related safety signal;
- a verified relationship from commanded waveform to measured output and evoked force;
- acceptable continuity and user-control performance; and
- honest classification as autonomous, PV-assisted, or hybrid based on WP1 and WP4 energy evidence.

If muscle volume is preserved but strength is not, the conclusion must remain “partial structural maintenance,” not “preserved muscle function.”

---

## 12. WP5 — Relevant-environment integration

### 12.1 Preconditions

WP5 begins only after G0–G4 evidence is reviewed by independent medical, electrical, battery, human-factors, and mission-safety specialists.

### 12.2 Progressive environments

1. integrated thermal, humidity, cleaning, flammability, and electromagnetic-compatibility testing;
2. habitat analog with higher-fidelity communication delay and power constraints;
3. short-duration altered-gravity or parabolic testing with stimulation disabled first;
4. altered-gravity testing of approved stationary stimulation only; and
5. a tightly scoped in-flight pilot after flight qualification and agency approval.

The first flight objective should be safety, fit, don/doff, contact stability, telemetry integrity, and evoked-force characterization—not a claim of long-term efficacy from a tiny astronaut sample. A current NASA head-down-bed-rest project also treats electrical muscle stimulation as a promising countermeasure requiring controlled evaluation, which supports this staged approach [12].

---

## 13. Safety, ethics, and governance

### 13.1 Governing principles

- participant welfare has priority over energy-autonomy targets;
- energy scarcity must never cause the controller to compensate with a more painful or hazardous waveform;
- safety-critical functions must not depend on cloud connectivity, a learned model, or a graphical display;
- users must be able to refuse or terminate a session without penalty;
- physiological data and inferred fatigue state are sensitive health data; and
- investigational use requires ethics approval, medical oversight, and an appropriate certified or verified stimulation platform.

### 13.2 Standards and design controls

The programme should map requirements to the current applicable editions of:

- IEC 60601-1 for basic safety and essential performance of medical electrical equipment;
- IEC 60601-2-10 for nerve and muscle stimulators [13];
- relevant IEC 60601 collateral standards for EMC, alarms, and usability as applicable;
- ISO 14971 for medical-device risk management;
- IEC 62304 for safety-relevant medical-device software where applicable;
- IEC 62366-1 for usability engineering where applicable;
- biocompatibility standards for prolonged skin contact;
- battery transport, protection, and habitat-specific fire-safety requirements; and
- NASA-STD-3001 and programme-specific human-system requirements for an eventual flight system [10].

Standards applicability must be confirmed by qualified regulatory and spaceflight-safety personnel; this framework is not a certification determination.

### 13.3 Independent safety layers

Minimum independent protections include:

- constant-current, charge-balanced output;
- hardware current and pulse-charge clamp;
- maximum session and daily dose counter;
- output watchdog and fail-open switching;
- isolation between PV/storage, communications, and electrodes;
- contact-quality and electrode-lift detection;
- thermal cutoffs;
- posture and movement interlock;
- local physical stop independent of software UI;
- no remote start;
- authenticated configuration and signed firmware; and
- complete immutable safety-event logging.

### 13.4 Session safety procedure

1. Confirm eligibility and absence of new contraindication or illness.
2. Inspect skin and verify electrode identity and location.
3. Confirm safe supported posture and protected schedule window.
4. Run electrical, storage, contact, temperature, and watchdog self-tests.
5. Display target muscles, purpose, dose range, expected duration, energy source, and stop method.
6. Obtain affirmative user start.
7. Ramp within the individual approved envelope.
8. Monitor output, force proxy, posture, contact, temperature, discomfort, and faults.
9. Stop on user request or any predefined limit.
10. Reinspect skin, record symptoms, and schedule delayed follow-up.

### 13.5 Adverse-event and stopping plan

The final protocol must define numerical and clinical stopping thresholds before ethics submission. At minimum, it must address:

- pain above the prespecified limit or sudden pain;
- skin burn, blister, persistent erythema, or allergic response;
- unexpected loss of motor control or unsafe limb movement;
- abnormal cardiovascular or neurological symptoms;
- excessive muscle soreness, weakness, swelling, dark urine, or laboratory evidence concerning for muscle injury;
- output waveform outside tolerance;
- high or unstable contact impedance;
- skin-facing or battery temperature above limit;
- repeated unexplained device reset or watchdog event; and
- any participant request to pause or stop.

An independent medical monitor or data and safety monitoring structure should adjudicate relatedness, severity, resumption, and programme-wide pauses.

---

## 14. Human factors and Space-HCI research frame

### 14.1 Design principles

1. **Legibility:** show where, why, how strongly, and for how long stimulation will occur.
2. **Preview before action:** never begin from a hidden or ambient state.
3. **Reversibility:** pause and stop are immediate, local, and always available.
4. **Calibrated trust:** expose uncertainty, energy shortfall, sensor faults, and incomplete dose.
5. **Protected attention:** stimulation is scheduled away from critical or precision work.
6. **Bodily autonomy:** remote clinicians may recommend but cannot silently initiate or escalate.
7. **Resource transparency:** distinguish harvested, stored, and central-grid energy.
8. **Graceful degradation:** loss of PV, a sensor, or communications reduces capability safely rather than increasing risk.

### 14.2 Interface information model

Before a session, display:

- purpose: “contingency muscle-maintenance session”;
- target muscles;
- planned duration and contraction/rest pattern;
- individualized intensity band and expected sensation;
- stored energy, expected energy use, reserve, and source provenance;
- reason for scheduling now;
- limitations: “does not replace today's full exercise session”; and
- pause and physical-stop instructions.

After a session, display:

- prescribed versus delivered dose;
- muscles and channels completed;
- interruptions, faults, or user changes;
- harvested and total energy consumed;
- next eligible session and recovery requirement; and
- symptoms that require medical contact.

### 14.3 Key HCI measures

- state/reason comprehension accuracy;
- stop-control discovery and latency;
- error recovery without external help;
- task workload;
- perceived control and coercion;
- appropriate reliance under correct and incorrect forecasts;
- alarm burden;
- explanation usefulness;
- willingness to use during a genuine outage; and
- discrepancy between logged behavior and retrospective account.

---

## 15. Data architecture and reproducibility

### 15.1 Minimum synchronized session record

```text
study_id, participant_id, garment_id, firmware_version, controller_version
session_id, timestamp_utc, mission_scenario, body_posture
channel_id, target_muscle, electrode_id, placement_template_version
commanded_current, measured_current, measured_voltage
pulse_shape, pulse_width, frequency, train_phase, duty_cycle, pulse_count
contact_quality, impedance, skin_temperature, electronics_temperature
evoked_torque_or_force, MVC_reference, discomfort, fatigue
PV_power, PV_energy, storage_in_energy, storage_out_energy
state_of_charge, state_of_health, energy_source_provenance
controller_decision, decision_reason, constraint_active
user_confirm, user_pause, user_stop, fault_code, session_stop_reason
skin_pre, skin_post, delayed_skin_followup, adverse_event_id
```

Sampling rates, clock synchronization, units, resolution, calibration, acceptable error, and missing-data codes must be specified in a data dictionary.

### 15.2 Reproducibility plan

- preregister human protocols and analysis plans;
- publish the intended-use statement and system boundary;
- version-control hardware, firmware, controller, placement templates, and prescriptions;
- archive calibration and uncertainty records;
- share de-identified data and analysis code where consent and security permit;
- publish negative energy, usability, and physiological results;
- report all tested illumination scenarios, not only the best one; and
- use CONSORT/SPIRIT-aligned reporting for the controlled trial and appropriate mixed-method guidance for WP3.

---

## 16. Decision logic and falsification criteria

The project is scientifically useful only if it can produce a clear negative conclusion.

| Evidence pattern | Required conclusion |
|---|---|
| Active NMES does not attenuate the primary muscle outcome | Reject the proposed physiological safety-net claim for the tested regimen and duration. |
| NMES attenuates muscle-volume loss but not strength loss | Claim partial structural maintenance only; do not claim preserved function. |
| NMES works, but $EAR<1$ in the declared scenario | Retain the NMES finding; rename system PV-assisted or hybrid. |
| PV is sufficient only when panels are removed and deployed | Describe it as a deployable garment charging system, not continuous on-body harvesting. |
| Energy-aware control saves energy but reduces dose beyond the margin | Reject dose non-inferiority; revise scheduling or increase storage/collection. |
| Users cannot reliably understand or stop the system | Stop operational development regardless of physiological benefit. |
| Recurrent skin, muscle-damage, motion, battery, or electrical hazard | Stop or redesign before further exposure. |
| All gates pass only under terrestrial illumination | Limit the claim to that test environment pending mission-specific validation. |

### 16.1 Recommended headline decision metric

The integrated concept advances only if it demonstrates:

> **verified physiological dose + bounded safety + preserved user agency + scenario-specific energy continuity**

No one term can compensate for failure of another.

---

## 17. Expected contributions

### Scientific

- evidence on whether NMES provides partial protection during a time-bounded exercise interruption;
- a dose model linking measured waveform, evoked force, energy, and fatigue;
- evidence separating preservation of muscle structure from strength and function; and
- a reusable method for resource-constrained physiological countermeasures.

### Engineering

- a full energy audit from incident light to evoked torque;
- safety architecture for isolated PV-powered stimulation;
- robust energy-aware scheduling under intermittent supply; and
- durability evidence for PV, electrodes, connectors, cleaning, sweat, and garment deformation.

### Space HCI

- design principles for transparent allocation of scarce environmental resources to the body;
- empirical measures of bodily agency in adaptive wearables;
- interface patterns for preview, consent, explanation, and graceful degradation; and
- a concrete model of clothing as distributed habitat infrastructure.

---

## 18. Principal limitations

- Head-down-tilt bed rest does not reproduce every physiological or operational feature of microgravity.
- Fourteen-day results cannot establish protection over months or years.
- Healthy volunteers are not astronauts, and astronaut samples are too small for conventional confirmatory inference.
- Sham blinding is imperfect when active contraction is obvious.
- Muscle volume, strength, endurance, coordination, bone loading, and cardiovascular fitness are distinct outcomes.
- Surface NMES recruitment and fatigue differ from voluntary exercise.
- Light exposure is highly site-, season-, spectrum-, orientation-, dust-, and operation-dependent.
- Photovoltaic and battery performance measured on Earth requires mission-specific environmental correction and validation.
- Added mass, heat, stiffness, cleaning burden, and maintenance may exceed the value of harvested energy.
- A distributed system may add failure modes even as it reduces dependence on centralized equipment.

---

## 19. Proposed programme outputs

1. Intended-use, non-use, and hazard-control specification.
2. Open energy-budget model with raw PV and load profiles.
3. Verified modular garment prototype and bench report.
4. Acute NMES safety, force, fatigue, and energy dataset.
5. Habitat-analog mixed-method study.
6. Preregistered head-down-bed-rest protocol and statistical analysis plan.
7. Controlled efficacy and energy-continuity results.
8. Human-factors design guidelines for resource-aware physiological wearables.
9. TRL evidence package and independent go/no-go review.

---

## 20. Paper framing

### Suggested paper claim

> We argue that off-world health garments should be designed as distributed, resource-aware physiological infrastructure. The Superman Suit materializes this position as a metabolic safety net: a bounded and user-controlled contingency layer that keeps limited muscle care conceptually available when centralized exercise infrastructure is interrupted.

### Suggested contribution statement

> Our contribution is not a validated muscle countermeasure. It is intermediate-level design knowledge: a theory-bearing artifact, seven design propositions, an evidence-bound computational probe, and a staged research agenda connecting intermittent resources, wearable infrastructure, bodily actuation, and crew agency.

### Suggested short subtitle

**A contingency layer, not an exercise replacement**

---

## References

1. Rivas, E., Strock, N., Dillon, E. L., & Frisco, D. *Risk of Impaired Performance Due to Reduced Muscle Mass, Strength, & Endurance and Risk of Reduced Physical Performance Capabilities Due to Reduced Aerobic Capacity* (Evidence Report HRP-47072). NASA Human Research Program, 2023. [NTRS record](https://ntrs.nasa.gov/citations/20220019338).
2. European Space Agency. *Weightless squats with the EasyMotion suit*. 25 April 2022. [ESA record](https://www.esa.int/ESA_Multimedia/Images/2022/04/Weightless_squats_with_the_EasyMotion_suit).
3. Hansen, S. K., et al. “Five days of bed rest in young and old adults: Retainment of skeletal muscle mass with neuromuscular electrical stimulation.” *Physiological Reports* 12(16), e16166, 2024. [https://doi.org/10.14814/phy2.16166](https://doi.org/10.14814/phy2.16166).
4. Doerr, D. F. *Electromyostimulation, Circuits and Monitoring*. NASA-TM-110741, 1994. [NTRS record](https://ntrs.nasa.gov/citations/19950024425).
5. Smith, J. D., Cromwell, R. L., Kundrot, C. E., & Charles, J. B. “Six-Degree Head-Down Tilt Bed Rest: Forty Years of Development as a Physiological Analog for Weightlessness.” [NTRS record](https://ntrs.nasa.gov/citations/20160002087).
6. Zhang, Z., et al. “A Wearable All-Solid Photovoltaic Textile.” *Advanced Materials* 28(13), 2639–2643, 2016. [https://doi.org/10.1002/adma.201504137](https://doi.org/10.1002/adma.201504137).
7. Chen, J., et al. “Micro-cable structured textile for simultaneously harvesting solar and mechanical energy.” *Nature Energy* 1, 16138, 2016. [https://doi.org/10.1038/nenergy.2016.138](https://doi.org/10.1038/nenergy.2016.138).
8. NASA. *The Harsh Environment of the Lunar South Pole*. [NASA reference](https://www.nasa.gov/reference/moonbase-environment/).
9. NASA Science. *10 Things: Massive Dust Storm on Mars*. [NASA Science](https://science.nasa.gov/solar-system/planets/mars/10-things-massive-dust-storm-on-mars/).
10. NASA. *NASA Spaceflight Human-System Standard, Volume 2: Human Factors, Habitability, and Environmental Health*. [NASA-STD-3001 Volume 2](https://www.nasa.gov/reference/nasa-std-3001v2/).
11. NASA. *Technology Readiness Levels*. [NASA reference](https://www.nasa.gov/directorates/somd/space-communications-navigation-program/technology-readiness-levels/).
12. Mortreux, M., et al. *Sensorimotor Countermeasures Head-Down Bed-Rest Study: Countermeasures for Mitigation of Sensorimotor Decrements Following Head-Down Bed Rest*. NASA Human Research Program Investigators' Workshop, 2026. [NTRS record](https://ntrs.nasa.gov/citations/20260002566).
13. International Electrotechnical Commission. *IEC 60601-2-10:2012+A1:2016+A2:2023 — Particular requirements for the basic safety and essential performance of nerve and muscle stimulators*. [IEC catalogue](https://webstore.iec.ch/en/publication/81814).
14. NASA. “Advanced Resistive Exercise Device Cable Fraying.” *ISS Daily Summary Report*, 25 November 2014. [NASA report](https://www.nasa.gov/blogs/stationreport/2014/11/25/iss-daily-summary-report-11-25-14/).
15. Svetlik, R. G., Moore, C., & Williams, A. *Practical Applications of Cables and Ropes in the ISS Countermeasures System*. 2017 IEEE Aerospace Conference. [NTRS record](https://ntrs.nasa.gov/citations/20160008095).
16. SpaceCHI. *SpaceCHI 2026: Submission Guidelines*. Accessed 18 July 2026. [Official conference page](https://spacechi.media.mit.edu/).
17. Hevner, A. R., March, S. T., Park, J., & Ram, S. “Design Science in Information Systems Research.” *MIS Quarterly* 28(1), 75–105, 2004. [AIS eLibrary record](https://aisel.aisnet.org/misq/vol28/iss1/6/).
18. Zimmerman, J., Forlizzi, J., & Evenson, S. “Research through Design as a Method for Interaction Design Research in HCI.” *Proceedings of CHI 2007*, 493–502. [https://doi.org/10.1145/1240624.1240704](https://doi.org/10.1145/1240624.1240704).
19. Gaver, W. “What Should We Expect from Research through Design?” *Proceedings of CHI 2012*, 937–946. [https://doi.org/10.1145/2207676.2208538](https://doi.org/10.1145/2207676.2208538).
20. Höök, K., & Löwgren, J. “Strong Concepts: Intermediate-Level Knowledge in Interaction Design Research.” *ACM Transactions on Computer-Human Interaction* 19(3), Article 23, 2012. [https://doi.org/10.1145/2362364.2362371](https://doi.org/10.1145/2362364.2362371).

---

## Research-status note

This document is primarily a design-science position-paper framework. It is not a clinical prescription, completed empirical study, medical-device certification, or flight-safety approval. The computational probe supplies bounded design evidence only. All future stimulation parameters, eligibility criteria, stop thresholds, environmental assumptions, and sample sizes require review by qualified clinical, engineering, ethics, and mission-safety teams before human use.
