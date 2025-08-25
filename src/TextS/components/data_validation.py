import os
from TextS.logging import Logger
from TextS.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exists(self) -> bool:
        try:
            # Use config for dataset directory
            dataset_dir = self.config.root_dir
            all_files = set(os.listdir(dataset_dir))

            required_files = set(self.config.ALL_REQUIRED_FILES)
            missing_files = required_files - all_files

            validation_status = len(missing_files) == 0

            # Write status to file
            with open(self.config.STATUS_FILE, 'w') as f:
                if validation_status:
                    f.write("Validation status: True\nAll required files are present.")
                    Logger.info("All required files are present.")
                else:
                    f.write(f"Validation status: False\nMissing files: {', '.join(missing_files)}")
                    Logger.warning(f"Missing files: {', '.join(missing_files)}")

            return validation_status

        except Exception as e:
            Logger.error(f"Validation failed: {e}")
            raise e