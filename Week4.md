# Commentary

## Transition from Analysis to Design
- Multiple implementations for requirements; choosing the best is challenging.
- Interactions between implementations and overall system behavior are often unclear until completion.
- Analysis models lay the foundation for design models.
- Design phase details data structures, architecture, interfaces, and components.

## Object-Oriented Class Diagram Design
- OO development is iterative: requirements, design, code, test.
- Analysis models evolve into design models.
- Classes and objects from analysis are refined and expanded in design.
- Relationships between classes are modeled: hierarchy, superclasses, subclasses.

### Best Practices for Identifying Object Classes
- Analyze grammatical content of problem statements/use cases; nouns suggest objects/attributes.
- Identify tangible entities and data storage structures.
- Review behavioral diagrams for key participants.
- Review scenario diagrams for data objects, attributes, and participants.

## Example Class Design
- Specify interface, signature, and semantics of object services.
- Include these descriptions in class diagrams.

### Types of Relationships in Class Diagrams
- **Association**: Necessary relationship with another class.
- **Aggregation**: Links a class with a collection.
- **Generalization**: Inheritance relationship with superclass.
- Associations can have navigability arrows for direction/ownership.
- Multiplicity shows possible instances of classes.

# Chapter 8

## What Makes a Good Design?
- Good design is characterized by multiple attributes, not a single definition.
- Two key characteristics: **Consistency** and **Completeness**.
- Consistency: Common terminology, error handling, navigational flow, and logic across the system.
- Completeness: All requirements are designed and carried out to sufficient detail.

## Measuring Design Complexity
- Early metrics focused on detail design and coding, not architecture.

### Halstead Complexity Metric
- Measures lexical complexity using operators and operands.
- Key units: n1 (distinct operators), n2 (distinct operands), N1 (total operator occurrences), N2 (total operand occurrences).
- Derived metrics: Program vocabulary (n), Program length (N), Volume (V), Potential volume (V@), Implementation level (L), Effort (E).
- Criticized for measuring only lexical complexity, not structure or logic.

### McCabe's Cyclomatic Complexity
- Measures control flow complexity: Cyclomatic complexity = E – N + 2p (edges, nodes, connected components).
- Also: number of binary decisions + 1, or number of closed regions + 1.
- Higher cyclomatic complexity = higher risk and more testing needed.
- Indicates number of linearly independent paths (test cases).

### Henry-Kafura Information Flow
- Measures intermodular flow: fan-in (info into module), fan-out (info out of module).
- Complexity Cp = (fan-in × fan-out)^2 for each module; sum for total system.
- Later modified to include internal complexity (e.g., cyclomatic, Halstead).

### Card and Glass Higher-Level Complexity
- Uses fan-in and fan-out for structural, data, and system complexity.
- System complexity = structural + data complexity.
- Focuses mostly on fan-out.

## Simplicity, Cohesion, and Coupling
- Simplicity achieved by decomposition into smaller, manageable pieces.
- **Cohesion**: Degree to which elements within a unit are related (strong cohesion is desirable).
- **Coupling**: Degree of interdependence between units (loose coupling is desirable).

### Cohesion
- Seven categories (from worst to best): Coincidental, Logical, Temporal, Procedural, Communicational, Sequential, Functional.
- Quantitative measures: Weak functional cohesion = glue tokens / total data tokens; Strong functional cohesion = superglue tokens / total data tokens.
- Example: Focusing a procedure on a single function increases cohesion.

### Coupling
- Five levels (from worst to best): Content, Common, Control, Stamp, Data coupling.
- Tight coupling makes reuse, maintenance, and testing harder; loose coupling is preferred.
- Pairwise coupling metric: C(x, y) = i + [n/(n + 1)], where i = highest coupling level, n = number of relationships.
- Global system coupling is the median of all pairwise couplings.

## Object-Oriented Design Metrics (C-K Metrics)
- Weighted Methods per Class (WMC): Sum of method weights; larger WMC = more error-prone.
- Depth of Inheritance Tree (DIT): Length from class to root; deeper trees may increase defects.
- Number of Children (NOC): Immediate subclasses; effect on quality is mixed.
- Coupling Between Object Classes (CBO): Number of coupled classes; higher CBO = more complexity.
- Response for a Class (RFC): Methods involved in response to a message; correlated with CBO and WMC.
- Lack of Cohesion in Methods (LCOM): Difference between method pairs with/without common variables; high LCOM = weak cohesion.
- Strive for strong cohesion and loose coupling.

## Aspect-Oriented Programming (AOP)
- Separation of concerns/aspects for modular, cohesive, and well-defined interfaces.
- Cross-cutting concerns are modularized into cohesive units.

## Law of Demeter
- Guideline for OO design: Objects should only communicate with immediate neighbors (attributes, parameters, created/returned objects).
- Reduces coupling and enhances cohesion.

## User Interface (UI) Design
- Consistency is crucial for user-friendliness.
- Three golden rules (Mandel): Place user in control, reduce memory load, design consistent UI.
- Additional principles: Actions should be interruptible/redoable, defaults should be meaningful.
- Eight rules (Shneiderman & Plaisant):
  1. Strive for consistency
  2. Enable shortcuts for frequent users
  3. Offer informative feedback
  4. Design dialogues for closure
  5. Prevent errors and offer simple error handling
  6. Permit easy reversal of actions
  7. Support internal locus of control
  8. Reduce short-term memory load
- UI guidelines and standards exist (IBM, Microsoft, Apple, ISO 9241).

## Usability Evaluation and Testing
- Usability testing moved earlier in development (requirements/design phases).
- Key factors: task completion rate, time to complete, help usage, redo frequency, shortcut usage.
- Early resolution of usability issues improves product quality.
