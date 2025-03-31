# Security Code Review Template

## Input Validation
- [ ] All user inputs are properly validated
- [ ] Input validation is done on server-side (not just client-side)
- [ ] SQL/NoSQL injection protections are in place
- [ ] XSS vulnerabilities are addressed

## Authentication & Authorization
- [ ] Authentication mechanisms are secure
- [ ] Password storage follows best practices (hashing, salting)
- [ ] Access controls are properly implemented
- [ ] Session management is secure
- [ ] JWT or tokens are properly handled

## Data Protection
- [ ] Sensitive data is properly encrypted
- [ ] Encryption algorithms are up-to-date and secure
- [ ] No sensitive information in logs or error messages
- [ ] Data in transit is encrypted (HTTPS/TLS)
- [ ] No hardcoded secrets, API keys, or credentials

## Dependency Security
- [ ] Third-party libraries are up-to-date
- [ ] Dependencies are from reliable sources
- [ ] No known vulnerabilities in dependencies

## API Security
- [ ] API endpoints have proper authentication
- [ ] Rate limiting is implemented
- [ ] API requests and responses are validated

## Security Risk Assessment
*Severity level (Critical, High, Medium, Low):*

## Recommended Mitigations
*Specific actions needed to address security concerns:*