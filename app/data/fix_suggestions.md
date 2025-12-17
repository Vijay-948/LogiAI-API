# Java Backend Error Fixes

## NullPointerException
Cause:
- Object is not initialized
- Bean injection failed

Fix:
- Add null checks
- Verify @Autowired beans
- Enable constructor injection

## OutOfMemoryError
Cause:
- JVM heap exhausted
- Memory leak

Fix:
- Increase heap size (-Xmx)
- Analyze heap dump
- Fix memory leaks

## Connection Refused
Cause:
- Database down
- Wrong host or port
- Firewall blocking connection

Fix:
- Verify DB URL
- Check port availability
- Restart database
