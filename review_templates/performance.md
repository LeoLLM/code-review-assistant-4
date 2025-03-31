# Performance Code Review Template

## Algorithm Efficiency
- [ ] Algorithms are optimized for the specific use case
- [ ] Time complexity is appropriate for the expected data size
- [ ] Space complexity is reasonable
- [ ] Loops and recursion are optimized

## Resource Management
- [ ] Memory usage is efficient
- [ ] Resources (files, connections, etc.) are properly closed
- [ ] Caching is used where appropriate
- [ ] Memory leaks are prevented

## Database Operations
- [ ] Database queries are optimized
- [ ] Indexes are properly utilized
- [ ] N+1 query problems are avoided
- [ ] Large result sets are handled efficiently (pagination, etc.)

## Frontend Performance
- [ ] Assets are minified and optimized
- [ ] Rendering performance is considered
- [ ] Network requests are minimized
- [ ] Lazy loading is implemented where appropriate

## Concurrency & Parallelism
- [ ] Threading or async operations are used effectively
- [ ] Race conditions are prevented
- [ ] Deadlocks are prevented
- [ ] Throttling/debouncing is used where appropriate

## Performance Metrics
- [ ] Expected performance characteristics are documented
- [ ] Critical operations have measurable performance goals
- [ ] Performance testing is included

## Optimization Recommendations
*Specific performance improvements suggested:*

## Performance Impact Assessment
*Expected impact of the changes on system performance:*