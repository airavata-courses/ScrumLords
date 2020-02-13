package com.postprocessor.Postprocessormicroservice;

import java.util.Map;

public interface PostProcessService {
  void getProcessedData();

  void getProcessedData(Map<String, Object> data);
}
