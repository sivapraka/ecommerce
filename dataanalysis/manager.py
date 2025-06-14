from .model import *
from .services import *
from .processor import DataAnalysisProcessor  # import your facade class


class DataAnalysisManager:
    def __init__(
        self,
        data_collection_service: DataCollectionService,
        data_preprocessing_service: DataPreprocessingService,
        analysis_algorithm_service: AnalysisAlgorithmService,
        visualization_service: VisualizationService,
    ):
        self.processor = DataAnalysisProcessor(
            data_collection_service,
            data_preprocessing_service,
            analysis_algorithm_service,
            visualization_service,
        )

    def perform_full_analysis(
        self,
        collection_params: DataCollectionParams,
        preprocessing_options: PreprocessingOptions,
        algorithm_config: AnalysisAlgorithmConfig,
    ) -> AnalysisResult:
        # Step 1: Collect data
        collection_result: DataCollectionResult = (
            self.processor.data_collection_service.collect_data(collection_params)
        )

        # Step 2: Preprocess data
        preprocessed_data: PreprocessedData = (
            self.processor.data_preprocessing_service.preprocess_data(
                collection_result.data, preprocessing_options
            )
        )

        # Step 3: Apply analysis algorithms
        analysis_result: AnalysisResult = (
            self.processor.analysis_algorithm_service.apply_analysis_algorithms(
                preprocessed_data, algorithm_config
            )
        )

        # Step 4: Visualize results
        self.processor.visualization_service.visualize_results(analysis_result)

        return analysis_result
