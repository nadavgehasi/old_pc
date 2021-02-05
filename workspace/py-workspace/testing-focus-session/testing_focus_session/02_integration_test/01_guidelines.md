# Guidelines
## Testing Flow:
1. Generating expected outputs
    - multiple test cases can be included in the outputs
2. Build Inputs from generated results
3. Run test using these inputs
4. Validate outputs are equal to expected outputs

## Alternatives:
- Constant input and outputs
    - More time to add new cases
    - Less cases will be tested
    - System may need test tear down
- Using input and outputs from production data
    - Hard to understand the expected results
    - A lot of configuration may be needed
    - Build new data sets from production can take long time

## Environments:
- Production (AKA. Critical E2E, Continues E2E)
- Development (AKA. Staging)
- Semi-Local - Using some cloud services
- Local
