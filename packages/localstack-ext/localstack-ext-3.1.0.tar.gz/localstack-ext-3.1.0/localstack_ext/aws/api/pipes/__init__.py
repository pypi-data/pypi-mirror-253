from datetime import datetime
from typing import Dict, List, Optional, TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Arn = str
ArnOrJsonPath = str
ArnOrUrl = str
BatchArraySize = int
BatchRetryAttempts = int
Boolean = bool
CapacityProvider = str
CapacityProviderStrategyItemBase = int
CapacityProviderStrategyItemWeight = int
Database = str
DbUser = str
EndpointString = str
EphemeralStorageSize = int
ErrorMessage = str
EventBridgeDetailType = str
EventBridgeEndpointId = str
EventBridgeEventSource = str
EventPattern = str
HeaderKey = str
HeaderValue = str
InputTemplate = str
Integer = int
JsonPath = str
KafkaTopicName = str
KinesisPartitionKey = str
LimitMax10 = int
LimitMax100 = int
LimitMax10000 = int
LimitMin1 = int
LogStreamName = str
MQBrokerQueueName = str
MaximumBatchingWindowInSeconds = int
MaximumRecordAgeInSeconds = int
MaximumRetryAttemptsESM = int
MessageDeduplicationId = str
MessageGroupId = str
NextToken = str
OptionalArn = str
PathParameter = str
PipeArn = str
PipeDescription = str
PipeName = str
PipeStateReason = str
PlacementConstraintExpression = str
PlacementStrategyField = str
QueryStringKey = str
QueryStringValue = str
ReferenceId = str
ResourceArn = str
RoleArn = str
SageMakerPipelineParameterName = str
SageMakerPipelineParameterValue = str
SecretManagerArn = str
SecretManagerArnOrJsonPath = str
SecurityGroup = str
SecurityGroupId = str
Sql = str
StatementName = str
String = str
Subnet = str
SubnetId = str
TagKey = str
TagValue = str
URI = str


class AssignPublicIp(str):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class BatchJobDependencyType(str):
    N_TO_N = "N_TO_N"
    SEQUENTIAL = "SEQUENTIAL"


class BatchResourceRequirementType(str):
    GPU = "GPU"
    MEMORY = "MEMORY"
    VCPU = "VCPU"


class DynamoDBStreamStartPosition(str):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"


class EcsEnvironmentFileType(str):
    s3 = "s3"


class EcsResourceRequirementType(str):
    GPU = "GPU"
    InferenceAccelerator = "InferenceAccelerator"


class KinesisStreamStartPosition(str):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"
    AT_TIMESTAMP = "AT_TIMESTAMP"


class LaunchType(str):
    EC2 = "EC2"
    FARGATE = "FARGATE"
    EXTERNAL = "EXTERNAL"


class MSKStartPosition(str):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"


class OnPartialBatchItemFailureStreams(str):
    AUTOMATIC_BISECT = "AUTOMATIC_BISECT"


class PipeState(str):
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    CREATING = "CREATING"
    UPDATING = "UPDATING"
    DELETING = "DELETING"
    STARTING = "STARTING"
    STOPPING = "STOPPING"
    CREATE_FAILED = "CREATE_FAILED"
    UPDATE_FAILED = "UPDATE_FAILED"
    START_FAILED = "START_FAILED"
    STOP_FAILED = "STOP_FAILED"


class PipeTargetInvocationType(str):
    REQUEST_RESPONSE = "REQUEST_RESPONSE"
    FIRE_AND_FORGET = "FIRE_AND_FORGET"


class PlacementConstraintType(str):
    distinctInstance = "distinctInstance"
    memberOf = "memberOf"


class PlacementStrategyType(str):
    random = "random"
    spread = "spread"
    binpack = "binpack"


class PropagateTags(str):
    TASK_DEFINITION = "TASK_DEFINITION"


class RequestedPipeState(str):
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"


class RequestedPipeStateDescribeResponse(str):
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    DELETED = "DELETED"


class SelfManagedKafkaStartPosition(str):
    TRIM_HORIZON = "TRIM_HORIZON"
    LATEST = "LATEST"


class ConflictException(ServiceException):
    code: str = "ConflictException"
    sender_fault: bool = True
    status_code: int = 409
    resourceId: String
    resourceType: String


class InternalException(ServiceException):
    code: str = "InternalException"
    sender_fault: bool = False
    status_code: int = 500
    retryAfterSeconds: Optional[Integer]


class NotFoundException(ServiceException):
    code: str = "NotFoundException"
    sender_fault: bool = True
    status_code: int = 404


class ServiceQuotaExceededException(ServiceException):
    code: str = "ServiceQuotaExceededException"
    sender_fault: bool = True
    status_code: int = 402
    quotaCode: String
    resourceId: String
    resourceType: String
    serviceCode: String


class ThrottlingException(ServiceException):
    code: str = "ThrottlingException"
    sender_fault: bool = True
    status_code: int = 429
    quotaCode: Optional[String]
    retryAfterSeconds: Optional[Integer]
    serviceCode: Optional[String]


class ValidationExceptionField(TypedDict, total=False):
    message: ErrorMessage
    name: String


ValidationExceptionFieldList = List[ValidationExceptionField]


class ValidationException(ServiceException):
    code: str = "ValidationException"
    sender_fault: bool = True
    status_code: int = 400
    fieldList: Optional[ValidationExceptionFieldList]


Subnets = List[Subnet]
SecurityGroups = List[SecurityGroup]


class AwsVpcConfiguration(TypedDict, total=False):
    AssignPublicIp: Optional[AssignPublicIp]
    SecurityGroups: Optional[SecurityGroups]
    Subnets: Subnets


class BatchArrayProperties(TypedDict, total=False):
    Size: Optional[BatchArraySize]


class BatchResourceRequirement(TypedDict, total=False):
    Type: BatchResourceRequirementType
    Value: String


BatchResourceRequirementsList = List[BatchResourceRequirement]


class BatchEnvironmentVariable(TypedDict, total=False):
    Name: Optional[String]
    Value: Optional[String]


BatchEnvironmentVariableList = List[BatchEnvironmentVariable]
StringList = List[String]


class BatchContainerOverrides(TypedDict, total=False):
    Command: Optional[StringList]
    Environment: Optional[BatchEnvironmentVariableList]
    InstanceType: Optional[String]
    ResourceRequirements: Optional[BatchResourceRequirementsList]


class BatchJobDependency(TypedDict, total=False):
    JobId: Optional[String]
    Type: Optional[BatchJobDependencyType]


BatchDependsOn = List[BatchJobDependency]
BatchParametersMap = Dict[String, String]


class BatchRetryStrategy(TypedDict, total=False):
    Attempts: Optional[BatchRetryAttempts]


class CapacityProviderStrategyItem(TypedDict, total=False):
    base: Optional[CapacityProviderStrategyItemBase]
    capacityProvider: CapacityProvider
    weight: Optional[CapacityProviderStrategyItemWeight]


CapacityProviderStrategy = List[CapacityProviderStrategyItem]


class PipeTargetStateMachineParameters(TypedDict, total=False):
    InvocationType: Optional[PipeTargetInvocationType]


class PipeTargetSqsQueueParameters(TypedDict, total=False):
    MessageDeduplicationId: Optional[MessageDeduplicationId]
    MessageGroupId: Optional[MessageGroupId]


class SageMakerPipelineParameter(TypedDict, total=False):
    Name: SageMakerPipelineParameterName
    Value: SageMakerPipelineParameterValue


SageMakerPipelineParameterList = List[SageMakerPipelineParameter]


class PipeTargetSageMakerPipelineParameters(TypedDict, total=False):
    PipelineParameterList: Optional[SageMakerPipelineParameterList]


Sqls = List[Sql]


class PipeTargetRedshiftDataParameters(TypedDict, total=False):
    Database: Database
    DbUser: Optional[DbUser]
    SecretManagerArn: Optional[SecretManagerArnOrJsonPath]
    Sqls: Sqls
    StatementName: Optional[StatementName]
    WithEvent: Optional[Boolean]


class PipeTargetLambdaFunctionParameters(TypedDict, total=False):
    InvocationType: Optional[PipeTargetInvocationType]


class PipeTargetKinesisStreamParameters(TypedDict, total=False):
    PartitionKey: KinesisPartitionKey


QueryStringParametersMap = Dict[QueryStringKey, QueryStringValue]
PathParameterList = List[PathParameter]
HeaderParametersMap = Dict[HeaderKey, HeaderValue]


class PipeTargetHttpParameters(TypedDict, total=False):
    HeaderParameters: Optional[HeaderParametersMap]
    PathParameterValues: Optional[PathParameterList]
    QueryStringParameters: Optional[QueryStringParametersMap]


EventBridgeEventResourceList = List[ArnOrJsonPath]


class PipeTargetEventBridgeEventBusParameters(TypedDict, total=False):
    DetailType: Optional[EventBridgeDetailType]
    EndpointId: Optional[EventBridgeEndpointId]
    Resources: Optional[EventBridgeEventResourceList]
    Source: Optional[EventBridgeEventSource]
    Time: Optional[JsonPath]


class Tag(TypedDict, total=False):
    Key: TagKey
    Value: TagValue


TagList = List[Tag]
PlacementStrategy = TypedDict(
    "PlacementStrategy",
    {
        "field": Optional[PlacementStrategyField],
        "type": Optional[PlacementStrategyType],
    },
    total=False,
)
PlacementStrategies = List[PlacementStrategy]
PlacementConstraint = TypedDict(
    "PlacementConstraint",
    {
        "expression": Optional[PlacementConstraintExpression],
        "type": Optional[PlacementConstraintType],
    },
    total=False,
)
PlacementConstraints = List[PlacementConstraint]


class EcsInferenceAcceleratorOverride(TypedDict, total=False):
    deviceName: Optional[String]
    deviceType: Optional[String]


EcsInferenceAcceleratorOverrideList = List[EcsInferenceAcceleratorOverride]


class EcsEphemeralStorage(TypedDict, total=False):
    sizeInGiB: EphemeralStorageSize


EcsResourceRequirement = TypedDict(
    "EcsResourceRequirement",
    {
        "type": EcsResourceRequirementType,
        "value": String,
    },
    total=False,
)
EcsResourceRequirementsList = List[EcsResourceRequirement]
EcsEnvironmentFile = TypedDict(
    "EcsEnvironmentFile",
    {
        "type": EcsEnvironmentFileType,
        "value": String,
    },
    total=False,
)
EcsEnvironmentFileList = List[EcsEnvironmentFile]


class EcsEnvironmentVariable(TypedDict, total=False):
    name: Optional[String]
    value: Optional[String]


EcsEnvironmentVariableList = List[EcsEnvironmentVariable]


class EcsContainerOverride(TypedDict, total=False):
    Command: Optional[StringList]
    Cpu: Optional[Integer]
    Environment: Optional[EcsEnvironmentVariableList]
    EnvironmentFiles: Optional[EcsEnvironmentFileList]
    Memory: Optional[Integer]
    MemoryReservation: Optional[Integer]
    Name: Optional[String]
    ResourceRequirements: Optional[EcsResourceRequirementsList]


EcsContainerOverrideList = List[EcsContainerOverride]


class EcsTaskOverride(TypedDict, total=False):
    ContainerOverrides: Optional[EcsContainerOverrideList]
    Cpu: Optional[String]
    EphemeralStorage: Optional[EcsEphemeralStorage]
    ExecutionRoleArn: Optional[ArnOrJsonPath]
    InferenceAcceleratorOverrides: Optional[EcsInferenceAcceleratorOverrideList]
    Memory: Optional[String]
    TaskRoleArn: Optional[ArnOrJsonPath]


class NetworkConfiguration(TypedDict, total=False):
    awsvpcConfiguration: Optional[AwsVpcConfiguration]


class PipeTargetEcsTaskParameters(TypedDict, total=False):
    CapacityProviderStrategy: Optional[CapacityProviderStrategy]
    EnableECSManagedTags: Optional[Boolean]
    EnableExecuteCommand: Optional[Boolean]
    Group: Optional[String]
    LaunchType: Optional[LaunchType]
    NetworkConfiguration: Optional[NetworkConfiguration]
    Overrides: Optional[EcsTaskOverride]
    PlacementConstraints: Optional[PlacementConstraints]
    PlacementStrategy: Optional[PlacementStrategies]
    PlatformVersion: Optional[String]
    PropagateTags: Optional[PropagateTags]
    ReferenceId: Optional[ReferenceId]
    Tags: Optional[TagList]
    TaskCount: Optional[LimitMin1]
    TaskDefinitionArn: ArnOrJsonPath


class PipeTargetCloudWatchLogsParameters(TypedDict, total=False):
    LogStreamName: Optional[LogStreamName]
    Timestamp: Optional[JsonPath]


class PipeTargetBatchJobParameters(TypedDict, total=False):
    ArrayProperties: Optional[BatchArrayProperties]
    ContainerOverrides: Optional[BatchContainerOverrides]
    DependsOn: Optional[BatchDependsOn]
    JobDefinition: String
    JobName: String
    Parameters: Optional[BatchParametersMap]
    RetryStrategy: Optional[BatchRetryStrategy]


class PipeTargetParameters(TypedDict, total=False):
    BatchJobParameters: Optional[PipeTargetBatchJobParameters]
    CloudWatchLogsParameters: Optional[PipeTargetCloudWatchLogsParameters]
    EcsTaskParameters: Optional[PipeTargetEcsTaskParameters]
    EventBridgeEventBusParameters: Optional[PipeTargetEventBridgeEventBusParameters]
    HttpParameters: Optional[PipeTargetHttpParameters]
    InputTemplate: Optional[InputTemplate]
    KinesisStreamParameters: Optional[PipeTargetKinesisStreamParameters]
    LambdaFunctionParameters: Optional[PipeTargetLambdaFunctionParameters]
    RedshiftDataParameters: Optional[PipeTargetRedshiftDataParameters]
    SageMakerPipelineParameters: Optional[PipeTargetSageMakerPipelineParameters]
    SqsQueueParameters: Optional[PipeTargetSqsQueueParameters]
    StepFunctionStateMachineParameters: Optional[PipeTargetStateMachineParameters]


TagMap = Dict[TagKey, TagValue]


class PipeSourceSqsQueueParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]


SubnetIds = List[SubnetId]
SecurityGroupIds = List[SecurityGroupId]


class SelfManagedKafkaAccessConfigurationVpc(TypedDict, total=False):
    SecurityGroup: Optional[SecurityGroupIds]
    Subnets: Optional[SubnetIds]


class SelfManagedKafkaAccessConfigurationCredentials(TypedDict, total=False):
    BasicAuth: Optional[SecretManagerArn]
    ClientCertificateTlsAuth: Optional[SecretManagerArn]
    SaslScram256Auth: Optional[SecretManagerArn]
    SaslScram512Auth: Optional[SecretManagerArn]


KafkaBootstrapServers = List[EndpointString]


class PipeSourceSelfManagedKafkaParameters(TypedDict, total=False):
    AdditionalBootstrapServers: Optional[KafkaBootstrapServers]
    BatchSize: Optional[LimitMax10000]
    ConsumerGroupID: Optional[URI]
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentials]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]
    ServerRootCaCertificate: Optional[SecretManagerArn]
    StartingPosition: Optional[SelfManagedKafkaStartPosition]
    TopicName: KafkaTopicName
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpc]


class MQBrokerAccessCredentials(TypedDict, total=False):
    BasicAuth: Optional[SecretManagerArn]


class PipeSourceRabbitMQBrokerParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    Credentials: MQBrokerAccessCredentials
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]
    QueueName: MQBrokerQueueName
    VirtualHost: Optional[URI]


class MSKAccessCredentials(TypedDict, total=False):
    ClientCertificateTlsAuth: Optional[SecretManagerArn]
    SaslScram512Auth: Optional[SecretManagerArn]


class PipeSourceManagedStreamingKafkaParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    ConsumerGroupID: Optional[URI]
    Credentials: Optional[MSKAccessCredentials]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]
    StartingPosition: Optional[MSKStartPosition]
    TopicName: KafkaTopicName


Timestamp = datetime


class DeadLetterConfig(TypedDict, total=False):
    Arn: Optional[Arn]


class PipeSourceKinesisStreamParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    DeadLetterConfig: Optional[DeadLetterConfig]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]
    MaximumRecordAgeInSeconds: Optional[MaximumRecordAgeInSeconds]
    MaximumRetryAttempts: Optional[MaximumRetryAttemptsESM]
    OnPartialBatchItemFailure: Optional[OnPartialBatchItemFailureStreams]
    ParallelizationFactor: Optional[LimitMax10]
    StartingPosition: KinesisStreamStartPosition
    StartingPositionTimestamp: Optional[Timestamp]


class Filter(TypedDict, total=False):
    Pattern: Optional[EventPattern]


FilterList = List[Filter]


class FilterCriteria(TypedDict, total=False):
    Filters: Optional[FilterList]


class PipeSourceDynamoDBStreamParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    DeadLetterConfig: Optional[DeadLetterConfig]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]
    MaximumRecordAgeInSeconds: Optional[MaximumRecordAgeInSeconds]
    MaximumRetryAttempts: Optional[MaximumRetryAttemptsESM]
    OnPartialBatchItemFailure: Optional[OnPartialBatchItemFailureStreams]
    ParallelizationFactor: Optional[LimitMax10]
    StartingPosition: DynamoDBStreamStartPosition


class PipeSourceActiveMQBrokerParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    Credentials: MQBrokerAccessCredentials
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]
    QueueName: MQBrokerQueueName


class PipeSourceParameters(TypedDict, total=False):
    ActiveMQBrokerParameters: Optional[PipeSourceActiveMQBrokerParameters]
    DynamoDBStreamParameters: Optional[PipeSourceDynamoDBStreamParameters]
    FilterCriteria: Optional[FilterCriteria]
    KinesisStreamParameters: Optional[PipeSourceKinesisStreamParameters]
    ManagedStreamingKafkaParameters: Optional[PipeSourceManagedStreamingKafkaParameters]
    RabbitMQBrokerParameters: Optional[PipeSourceRabbitMQBrokerParameters]
    SelfManagedKafkaParameters: Optional[PipeSourceSelfManagedKafkaParameters]
    SqsQueueParameters: Optional[PipeSourceSqsQueueParameters]


class PipeEnrichmentHttpParameters(TypedDict, total=False):
    HeaderParameters: Optional[HeaderParametersMap]
    PathParameterValues: Optional[PathParameterList]
    QueryStringParameters: Optional[QueryStringParametersMap]


class PipeEnrichmentParameters(TypedDict, total=False):
    HttpParameters: Optional[PipeEnrichmentHttpParameters]
    InputTemplate: Optional[InputTemplate]


class CreatePipeRequest(ServiceRequest):
    Description: Optional[PipeDescription]
    DesiredState: Optional[RequestedPipeState]
    Enrichment: Optional[OptionalArn]
    EnrichmentParameters: Optional[PipeEnrichmentParameters]
    Name: PipeName
    RoleArn: RoleArn
    Source: ArnOrUrl
    SourceParameters: Optional[PipeSourceParameters]
    Tags: Optional[TagMap]
    Target: Arn
    TargetParameters: Optional[PipeTargetParameters]


class CreatePipeResponse(TypedDict, total=False):
    Arn: Optional[PipeArn]
    CreationTime: Optional[Timestamp]
    CurrentState: Optional[PipeState]
    DesiredState: Optional[RequestedPipeState]
    LastModifiedTime: Optional[Timestamp]
    Name: Optional[PipeName]


class DeletePipeRequest(ServiceRequest):
    Name: PipeName


class DeletePipeResponse(TypedDict, total=False):
    Arn: Optional[PipeArn]
    CreationTime: Optional[Timestamp]
    CurrentState: Optional[PipeState]
    DesiredState: Optional[RequestedPipeStateDescribeResponse]
    LastModifiedTime: Optional[Timestamp]
    Name: Optional[PipeName]


class DescribePipeRequest(ServiceRequest):
    Name: PipeName


class DescribePipeResponse(TypedDict, total=False):
    Arn: Optional[PipeArn]
    CreationTime: Optional[Timestamp]
    CurrentState: Optional[PipeState]
    Description: Optional[PipeDescription]
    DesiredState: Optional[RequestedPipeStateDescribeResponse]
    Enrichment: Optional[OptionalArn]
    EnrichmentParameters: Optional[PipeEnrichmentParameters]
    LastModifiedTime: Optional[Timestamp]
    Name: Optional[PipeName]
    RoleArn: Optional[RoleArn]
    Source: Optional[ArnOrUrl]
    SourceParameters: Optional[PipeSourceParameters]
    StateReason: Optional[PipeStateReason]
    Tags: Optional[TagMap]
    Target: Optional[Arn]
    TargetParameters: Optional[PipeTargetParameters]


class ListPipesRequest(ServiceRequest):
    CurrentState: Optional[PipeState]
    DesiredState: Optional[RequestedPipeState]
    Limit: Optional[LimitMax100]
    NamePrefix: Optional[PipeName]
    NextToken: Optional[NextToken]
    SourcePrefix: Optional[ResourceArn]
    TargetPrefix: Optional[ResourceArn]


class Pipe(TypedDict, total=False):
    Arn: Optional[PipeArn]
    CreationTime: Optional[Timestamp]
    CurrentState: Optional[PipeState]
    DesiredState: Optional[RequestedPipeState]
    Enrichment: Optional[OptionalArn]
    LastModifiedTime: Optional[Timestamp]
    Name: Optional[PipeName]
    Source: Optional[ArnOrUrl]
    StateReason: Optional[PipeStateReason]
    Target: Optional[Arn]


PipeList = List[Pipe]


class ListPipesResponse(TypedDict, total=False):
    NextToken: Optional[NextToken]
    Pipes: Optional[PipeList]


class ListTagsForResourceRequest(ServiceRequest):
    resourceArn: PipeArn


class ListTagsForResourceResponse(TypedDict, total=False):
    tags: Optional[TagMap]


class StartPipeRequest(ServiceRequest):
    Name: PipeName


class StartPipeResponse(TypedDict, total=False):
    Arn: Optional[PipeArn]
    CreationTime: Optional[Timestamp]
    CurrentState: Optional[PipeState]
    DesiredState: Optional[RequestedPipeState]
    LastModifiedTime: Optional[Timestamp]
    Name: Optional[PipeName]


class StopPipeRequest(ServiceRequest):
    Name: PipeName


class StopPipeResponse(TypedDict, total=False):
    Arn: Optional[PipeArn]
    CreationTime: Optional[Timestamp]
    CurrentState: Optional[PipeState]
    DesiredState: Optional[RequestedPipeState]
    LastModifiedTime: Optional[Timestamp]
    Name: Optional[PipeName]


TagKeyList = List[TagKey]


class TagResourceRequest(ServiceRequest):
    resourceArn: PipeArn
    tags: TagMap


class TagResourceResponse(TypedDict, total=False):
    pass


class UntagResourceRequest(ServiceRequest):
    resourceArn: PipeArn
    tagKeys: TagKeyList


class UntagResourceResponse(TypedDict, total=False):
    pass


class UpdatePipeSourceSqsQueueParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]


class UpdatePipeSourceSelfManagedKafkaParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    Credentials: Optional[SelfManagedKafkaAccessConfigurationCredentials]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]
    ServerRootCaCertificate: Optional[SecretManagerArn]
    Vpc: Optional[SelfManagedKafkaAccessConfigurationVpc]


class UpdatePipeSourceRabbitMQBrokerParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    Credentials: MQBrokerAccessCredentials
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]


class UpdatePipeSourceManagedStreamingKafkaParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    Credentials: Optional[MSKAccessCredentials]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]


class UpdatePipeSourceKinesisStreamParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    DeadLetterConfig: Optional[DeadLetterConfig]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]
    MaximumRecordAgeInSeconds: Optional[MaximumRecordAgeInSeconds]
    MaximumRetryAttempts: Optional[MaximumRetryAttemptsESM]
    OnPartialBatchItemFailure: Optional[OnPartialBatchItemFailureStreams]
    ParallelizationFactor: Optional[LimitMax10]


class UpdatePipeSourceDynamoDBStreamParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    DeadLetterConfig: Optional[DeadLetterConfig]
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]
    MaximumRecordAgeInSeconds: Optional[MaximumRecordAgeInSeconds]
    MaximumRetryAttempts: Optional[MaximumRetryAttemptsESM]
    OnPartialBatchItemFailure: Optional[OnPartialBatchItemFailureStreams]
    ParallelizationFactor: Optional[LimitMax10]


class UpdatePipeSourceActiveMQBrokerParameters(TypedDict, total=False):
    BatchSize: Optional[LimitMax10000]
    Credentials: MQBrokerAccessCredentials
    MaximumBatchingWindowInSeconds: Optional[MaximumBatchingWindowInSeconds]


class UpdatePipeSourceParameters(TypedDict, total=False):
    ActiveMQBrokerParameters: Optional[UpdatePipeSourceActiveMQBrokerParameters]
    DynamoDBStreamParameters: Optional[UpdatePipeSourceDynamoDBStreamParameters]
    FilterCriteria: Optional[FilterCriteria]
    KinesisStreamParameters: Optional[UpdatePipeSourceKinesisStreamParameters]
    ManagedStreamingKafkaParameters: Optional[UpdatePipeSourceManagedStreamingKafkaParameters]
    RabbitMQBrokerParameters: Optional[UpdatePipeSourceRabbitMQBrokerParameters]
    SelfManagedKafkaParameters: Optional[UpdatePipeSourceSelfManagedKafkaParameters]
    SqsQueueParameters: Optional[UpdatePipeSourceSqsQueueParameters]


class UpdatePipeRequest(ServiceRequest):
    Description: Optional[PipeDescription]
    DesiredState: Optional[RequestedPipeState]
    Enrichment: Optional[OptionalArn]
    EnrichmentParameters: Optional[PipeEnrichmentParameters]
    Name: PipeName
    RoleArn: RoleArn
    SourceParameters: Optional[UpdatePipeSourceParameters]
    Target: Optional[Arn]
    TargetParameters: Optional[PipeTargetParameters]


class UpdatePipeResponse(TypedDict, total=False):
    Arn: Optional[PipeArn]
    CreationTime: Optional[Timestamp]
    CurrentState: Optional[PipeState]
    DesiredState: Optional[RequestedPipeState]
    LastModifiedTime: Optional[Timestamp]
    Name: Optional[PipeName]


class PipesApi:
    service = "pipes"
    version = "2015-10-07"

    @handler("CreatePipe")
    def create_pipe(
        self,
        context: RequestContext,
        name: PipeName,
        role_arn: RoleArn,
        source: ArnOrUrl,
        target: Arn,
        description: PipeDescription = None,
        desired_state: RequestedPipeState = None,
        enrichment: OptionalArn = None,
        enrichment_parameters: PipeEnrichmentParameters = None,
        source_parameters: PipeSourceParameters = None,
        tags: TagMap = None,
        target_parameters: PipeTargetParameters = None,
    ) -> CreatePipeResponse:
        raise NotImplementedError

    @handler("DeletePipe")
    def delete_pipe(self, context: RequestContext, name: PipeName) -> DeletePipeResponse:
        raise NotImplementedError

    @handler("DescribePipe")
    def describe_pipe(self, context: RequestContext, name: PipeName) -> DescribePipeResponse:
        raise NotImplementedError

    @handler("ListPipes")
    def list_pipes(
        self,
        context: RequestContext,
        current_state: PipeState = None,
        desired_state: RequestedPipeState = None,
        limit: LimitMax100 = None,
        name_prefix: PipeName = None,
        next_token: NextToken = None,
        source_prefix: ResourceArn = None,
        target_prefix: ResourceArn = None,
    ) -> ListPipesResponse:
        raise NotImplementedError

    @handler("ListTagsForResource")
    def list_tags_for_resource(
        self, context: RequestContext, resource_arn: PipeArn
    ) -> ListTagsForResourceResponse:
        raise NotImplementedError

    @handler("StartPipe")
    def start_pipe(self, context: RequestContext, name: PipeName) -> StartPipeResponse:
        raise NotImplementedError

    @handler("StopPipe")
    def stop_pipe(self, context: RequestContext, name: PipeName) -> StopPipeResponse:
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: PipeArn, tags: TagMap
    ) -> TagResourceResponse:
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self, context: RequestContext, resource_arn: PipeArn, tag_keys: TagKeyList
    ) -> UntagResourceResponse:
        raise NotImplementedError

    @handler("UpdatePipe")
    def update_pipe(
        self,
        context: RequestContext,
        name: PipeName,
        role_arn: RoleArn,
        description: PipeDescription = None,
        desired_state: RequestedPipeState = None,
        enrichment: OptionalArn = None,
        enrichment_parameters: PipeEnrichmentParameters = None,
        source_parameters: UpdatePipeSourceParameters = None,
        target: Arn = None,
        target_parameters: PipeTargetParameters = None,
    ) -> UpdatePipeResponse:
        raise NotImplementedError
