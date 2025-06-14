import unittest
from unittest.mock import patch
from dataanalysis.services import *
from dataanalysis.manager import DataAnalysisManager


class TestDataAnalysisManager(unittest.TestCase):
    DEPENDENCIES = {
        "data_collection_service",
        "data_preprocessing_service",
        "analysis_algorithm_service",
        "visualization_service",
    }

    def test_dependencies(self):
        data_analysis_manager = DataAnalysisManager(
            DataCollectionService(),
            DataPreprocessingService(),
            AnalysisAlgorithmService(),
            VisualizationService(),
        )

        dependencies_present = all(
            hasattr(data_analysis_manager, dep) for dep in self.DEPENDENCIES
        )

        self.assertFalse(
            dependencies_present,
            "If the facade pattern is implemented correctly, the DataAnalysisManager class should not have any dependencies on the services",
        )

    @patch.object(DataCollectionService, "collect_data", return_value=DataCollectionResult([]))
    @patch.object(DataPreprocessingService, "preprocess_data", return_value=PreprocessedData())
    @patch.object(
        AnalysisAlgorithmService, "apply_analysis_algorithms", return_value=AnalysisResult()
    )
    @patch.object(VisualizationService, "visualize_results")
    def test_perform_full_analysis(
        self,
        mock_visualize_results,
        mock_apply_analysis_algorithms,
        mock_preprocess_data,
        mock_collect_data,
    ):
        # Create a DataAnalysisManager instance
        data_analysis_manager = DataAnalysisManager(
            DataCollectionService(),
            DataPreprocessingService(),
            AnalysisAlgorithmService(),
            VisualizationService(),
        )

        # Define test data
        collection_params = DataCollectionParams()
        preprocessing_options = PreprocessingOptions()
        algorithm_config = AnalysisAlgorithmConfig()

        # Perform full analysis
        data_analysis_manager.perform_full_analysis(
            collection_params, preprocessing_options, algorithm_config
        )

        # Verify interactions with the dependencies
        mock_collect_data.assert_called_once_with(collection_params)
        mock_preprocess_data.assert_called_once()
        mock_apply_analysis_algorithms.assert_called_once()
        mock_visualize_results.assert_called_once()


if __name__ == "__main__":
    unittest.main()
