# Predicting Bridge Performance with NBI Data

Using publicly available data gleaned from the National Bridge Inventory (NBI), a classification model was developed to predict whether bridges' Sufficiency Ratings will fall to a Poor Rating after a fixed amount of time. The model was based on the following:
- Model input based on 191 NBI items
- Model prediction is binary: "poor" or "not poor"
- Dataset based on Virginia bridges (no culverts) from 2007
- Model predictions are for 2017 (ten-year time period)
- Initial Sufficiency Rating values between 50 and 79.9 (Fair Rating)
- Bridges with major repair work after 2007 were excluded

This analysis also explored what trends can be interpreted from specific bridge characteristics. Based on the model's interpretation:
- Variable correlated with better performance:
  - Higher initial Sufficiency Rating
  - Higher Superstructure Condition Rating
  - Concrete superstructure
  - Latex concrete wearing surface
  - Highway route underneath
- Variables correlated with worse performance:
  - Wood/timber deck
  - Undetermined historical significance
  - Structure part of minor urban artery
  - Structure posted for load
