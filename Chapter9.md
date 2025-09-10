# Chapter 9: Implementation Highlights

## 9.1 Introduction to Implementation

- Implementation is the process of transforming detailed design into a working program.
- In small projects, detailed design is often part of implementation; in larger projects, it is usually done separately.
- Implementation includes coding, testing, debugging, compiling, and configuration management.
- Not all modules require the same level of design detail; critical modules may be designed by experienced personnel.

## 9.2 Characteristics of a Good Implementation

- **Readability:** Code should be easily understood by others.
- **Maintainability:** Code should be easy to modify and maintain.
- **Performance:** Code should be efficient, but not at the expense of readability and maintainability.
- **Traceability:** Code elements should correspond to design elements.
- **Correctness:** Code should fulfill requirements and design.
- **Completeness:** All system requirements must be met.
- Trade-offs exist between these characteristics; for example, performance optimizations may reduce readability.

## 9.3 Programming Style and Coding Guidelines

- Most organizations have coding guidelines for naming, indentation, and commenting.
- Consistency in style is crucial for readability and maintainability.
- Naming conventions help clarify code intent; good names correlate with understanding.
- Use standard conventions for word separation and capitalization (e.g., underscores in C, camelCase in Java).
- Indentation and spacing are important for code structure and readability.
- Limit function/method size to around 50 lines for clarity.
- File-naming conventions aid in organization and integration.
- Some language features (e.g., GOTO, multiple inheritance) may be banned due to error-proneness.

## 9.4 Comments

- Comments aid readability and maintainability but can also distract or become outdated.
- Six types of comments:
  1. Repeat of the code (should be avoided)
  2. Explanation of the code (rewrite complex code instead)
  3. Marker in the code (use consistently, remove before production)
  4. Summary of the code (helpful if kept up to date)
  5. Description of code intent (most useful)
  6. External references (link code to external sources)
- Strive for self-documented code; use comments mainly for intent and external references.

## 9.5 Debugging

- Debugging involves locating and fixing errors, usually found through testing.
- Four phases of debugging:
  1. **Stabilization:** Reproduce the error and identify conditions.
  2. **Localization:** Find the code section causing the error.
  3. **Correction:** Change code to fix the error.
  4. **Verification:** Ensure the error is fixed and no new errors are introduced.
- Errors can be syntax or logic errors.
- Tools for debugging: source code comparators, extended checkers, interactive debuggers, safeguarded libraries, profilers, and coverage tools.

## 9.6 Assertions and Defensive Programming

- Assertions are used to make preconditions and postconditions explicit.
- Preconditions: Required conditions for correct results.
- Postconditions: Conditions that should hold after execution.
- Assertions help catch errors and can be used with formal methods for correctness.

## 9.7 Performance Optimization

- Performance is important but should not compromise correctness or maintainability.
- Optimize only after ensuring correctness and maintainability.
- Use profilers to identify bottlenecks and optimize only critical modules.
- Sometimes, simplifying code improves performance.
- Consider cost-benefit analysis before optimizing; sometimes hardware upgrades are preferable.
- Reuse high-quality code and standard libraries for performance.

## 9.8 Refactoring

- Refactoring improves code style without changing behavior.
- Martin Fowler popularized refactoring and cataloged "bad smells" indicating need for improvement.
- Common "bad smells": duplicated code, long methods, large classes, switch statements, feature envy, inappropriate intimacy.
- Refactoring techniques:
  - **Extract method:** Move code fragment to a new method.
  - **Substitute algorithm:** Replace method body with a clearer algorithm.
  - **Move method:** Move algorithm to a more appropriate class.
  - **Extract class:** Divide a class into two.
- Refactoring makes code easier to understand and cheaper to modify.
