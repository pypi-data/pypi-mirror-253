# This is for random seeds in numpy, which has some unfortunate
# weirdness with > 32 bit seeds
# e.g., https://stackoverflow.com/questions/36755940
MAX_INT_32 = 2147483647

LOG_VERBOSE = 1
LOG_PRODUCTION = 2
LOG_TENSORFLOW = 3

MAX_TREE_EMBEDDING_SIZE = 128
MAX_TREE_MODELS = 16

MAX_BOXES = 128
ANCHORS_PER_SIZE = 3
BOX_LABEL_SMOOTHING = 0.01
BACKGROUND_IOU = 0.3

FEATURES_FORMAT = "scale_%d_features"
BOXES_FORMAT = "scale_%d_boxes"

# Names for YOLO outputs from each branch for training
CONF_FORMAT = "scale_%d_confidence_outputs"
PROB_FORMAT = "scale_%d_probability_outputs"
GIOU_FORMAT = "scale_%d_giou_outputs"
CIOU_FORMAT = "scale_%d_ciou_outputs"
CENT_FORMAT = "scale_%d_center_outputs"

# Augmentations we can't use for bounding box detection
NON_BOX_AUGMENTATIONS = ["rotation", "shear"]

BG_CONSTANT = 42
BG_CONSTANT_PIXEL = [BG_CONSTANT, BG_CONSTANT, BG_CONSTANT]

DEFAULT_EXPORT_SETTINGS = {"output_unfiltered_boxes": True}

HOLDOUT_PREDICT_SETTINGS = {"iou_threshold": 0.2, "bounding_box_threshold": 0.3}
