from .model import (
    DataCollectionParams,
    PreprocessingOptions,
    AnalysisAlgorithmConfig,
    AnalysisResult
)
from .services import (
    DataCollectionService,
    DataPreprocessingService,
    AnalysisAlgorithmService,
    VisualizationService
)


class DataAnalysisProcessor:
    def __init__(
        self,
        data_collection_service: DataCollectionService,
        data_preprocessing_service: DataPreprocessingService,
        analysis_algorithm_service: AnalysisAlgorithmService,
        visualization_service: VisualizationService,
    ):
        self.data_collection_service = data_collection_service
        self.data_preprocessing_service = data_preprocessing_service
        self.analysis_algorithm_service = analysis_algorithm_service
        self.visualization_service = visualization_service

    def perform_full_analysis(
        self,
        collection_params: DataCollectionParams,
        preprocessing_options: PreprocessingOptions,
        algorithm_config: AnalysisAlgorithmConfig,
    ) -> AnalysisResult:
        # Step 1: Collect data
        collection_result = self.data_collection_service.collect_data(collection_params)

        # Step 2: Preprocess data
        preprocessed_data = self.data_preprocessing_service.preprocess_data(
            collection_result.data,
            preprocessing_options
        )

        # Step 3: Analyze data
        analysis_result = self.analysis_algorithm_service.apply_analysis_algorithms(
            preprocessed_data,
            algorithm_config
        )

        # Step 4: Visualize results
        self.visualization_service.visualize_results(analysis_result)

        return analysis_result
