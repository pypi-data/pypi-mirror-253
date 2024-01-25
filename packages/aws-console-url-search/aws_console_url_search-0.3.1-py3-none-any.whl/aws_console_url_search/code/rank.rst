Rank
==============================================================================


Design
------------------------------------------------------------------------------


1. Rank 指的是排序时的顺序, service 和 sub service 都有各自的 Rank. Rank 是一个整数, 数字越小, 搜索排序时就越靠前.
2. Service 的 Rank 是一个 1 - 10000 之间的整数, 这是因为目前 AWS 已经有 200 多个 Service 了. 为了虽然不太可能, 但应该不会超过 1000, 但是为了保险起见, 还是给了 10 倍上限, 也就是 10000 的空间
3. Sub Service 的 Rank 是一个 1 - 1000 之间的整数, 这是因为一个 Service 下的 Sub Service 不太可能超过 100 个, 但是为了保险起见, 还是给了 10 倍上限, 也就是 1000 的空间
4. 所有的 service 以及 sub service 排序, 都先看 service 的 Rank, 相等才看 sub service 的 Rank, 如果还是相等则看 service 的名字顺序. 名字只取前 10 个字符, 且忽略大小写.
5. 根据 #4, 所有的顶层 service 都排在 sub service 之前.


Service Rank
------------------------------------------------------------------------------
1. S3
2. IAM
3. EC2
4. VPC
5. DynamoDB
6. RDS
7. SNS
8. SQS
9. Lambda
10. CloudFormation
11. CloudWatch
12. ECR
13. Athena
14. SecretManager
15. KMS
16. Kinesis
17. SageMaker
18. StepFunction
19. CloudFront
20. Route53
21. ApiGateway
22. Cognito
23. ECS
24. Redshift
25. OpenSearch
26. CodeCommit
27. CodeBuild
28. CodePipeline
29. CodeDeploy
30. EMR
31. Glue
32. LakeFormation
33. QuickSight
34. DMS
35. ElasticCache
36. DocumentDB
37. MemoryDB
38. Keyspaces
39. TimeStream
40. Neptune
41. EFS
42. FSx
43. Glacier
44. ElasticBeanstalk
45. EKS
46. CloudTrail
47. SystemManager
48. EventBridge
49. CostManagement
