# Final Exercise

Access a specific sensor of opensensemap (https://www.opensensemap.org/).

- download the data and buffer it in Kafka. Read more often than the update interval of the sensor in order to compensate for possible failures of the service. (e.g. we want to be able to buffer 1 hour failure)
- by the failure compensation you will get duplicated values. We want to detect these in a stream processing pipline and save the cleaned up values in a separate topic.
- create a microservice that filters the messages / reads the only the measurement containing the particle size PM10.
- write a microservice that provides a small infographics (traffic light / circle) to show if the measured values are still within the range.

All code must be in Python. Code should be hosted and run on prepared Kafka Environment. Jupyter Lab notebooks can be written and run under http://127.0.0.1:28888 (login token: abc123!)
