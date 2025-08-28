# Chapter 7: Design – Architecture and Methodology

## Objectives
- Understand differences between architectural and detailed design
- Learn common software architectural styles, tactics, and reference architectures
- Learn basic techniques for detailed design: functional decomposition, relational database design, object-oriented design
- Understand basic issues in user-interface design

## 7.1 Introduction to Design
- Design transforms requirements into a structured plan for software
- Architectural design: high-level overview, main components, relationships, external properties
- Detailed design: decomposes components to finer detail, addresses all functional requirements
- Architecture drives detailed design; requirements influence architecture
- UML is the de facto standard for graphical design notation in OO design

## 7.2 Architectural Design
### What Is Software Architecture?
- Specifies basic structure of a system
- Every system has an architecture, explicit or not
- Large systems may have multiple structures (views)
- Architecture focuses on interfaces and relationships among modules

### Views and Viewpoints
- A view represents a system structure
- Multiple views are needed for a complete picture
- Kruchten's four architectural views:
  - Logical view: object-oriented decomposition (classes, relationships)
  - Process view: run-time components and communication
  - Subsystem decomposition view: modules and subsystems
  - Physical architecture view: mapping software to hardware
- Bass, Clements, Kazman: module views, run-time views, allocation views
- Different views serve different stakeholders

### Meta-Architectural Knowledge: Styles, Patterns, Tactics, Reference Architectures
- Architectural styles/patterns: common system structures
  - Pipes-and-filters: processes connected by pipes, output of one is input to next
  - Event-driven: components react to events, communicate via events
  - Client-server: clients and servers interact over a network
  - Model-view-controller (MVC): separates data (model) from display (view)
  - Layered: components grouped into layers, communicate with adjacent layers
  - Database-centric: central database, programs access via DBMS
  - Three-tier: adds middle tier for business logic between clients and database
- Architectural tactics: solve specific problems, e.g., fault detection (heartbeat, ping/echo)
- Reference architectures: templates for related systems, with defined points of variation

## 7.3 Detailed Design
- Refines architecture and requirements into implementable modules
- Level of detail depends on development process

### Functional Decomposition
- Decompose functions/modules into smaller modules
- Used in structured programming and initial OO decomposition
- Module decomposition diagrams show hierarchy and relationships
- Design alternatives affect cohesion and coupling

### Relational Database Design
- Information stored in tables (relations) with rows and columns
- Four phases:
  - Data modeling: create entity-relationship (ER) model
  - Logical database design: produce normalized relational schema
  - Physical database design: choose data types, indexes, optimize schema
  - Deployment and maintenance: finalize details, optimize performance
- ER diagrams: entities, attributes, relationships
- Transform entities and relationships into tables
- Normalization minimizes redundancy

### Object-Oriented Design and UML
- Use cases and class diagrams document OO design
- Classes: group objects with similar structure and behavior
- Encapsulation: data and methods included in objects
- UML class diagrams: show class name, attributes, methods
- Associations: relationships between classes, navigability
- Aggregation and composition: part-of relationships
- Inheritance: subclasses inherit attributes and methods from superclasses
- State modeling: use state transition diagrams to represent object states
- Interactions: sequence diagrams show message flow among objects

### User-Interface Design
- UI is critical for user experience
- Prototypes (low/high fidelity) validate design with users
- Two main issues: flow of interactions and look and feel
- Flow of interactions maps to use cases and sequence diagrams
- Cognitive models (e.g., GOMS) help design user-centered interfaces
- Good UI design uses consistency, user control, reduced memory load, visible system status

---

These notes summarize the key concepts and techniques from Chapter 7, focusing on software design, architecture, and methodology.
