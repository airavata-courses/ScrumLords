package com.postprocessor.Postprocessormicroservice;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;
import java.util.HashMap;
import java.util.Map;
import org.apache.tomcat.util.codec.binary.Base64;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PostprocessorController {

  @Autowired private PostProcessService postprocessService;

  @RequestMapping(value = "/process/analyze", method = RequestMethod.POST)
  public ResponseEntity<?> postprocess(@RequestBody Map<String, Object> data) {

    Map<String, Object> dataObj = (Map<String, Object>) data.get("message");

    String dataObj2 = dataObj.get("data").toString();

    byte[] byteArrayData = Base64.decodeBase64(dataObj2.getBytes());
    String decodedData = new String(byteArrayData);

    HashMap<String, Object> datamap =
        new Gson().fromJson(decodedData, new TypeToken<HashMap<String, Object>>() {}.getType());

    Map<String, Object> datadict = new HashMap<String, Object>();

    datadict.put("data", datamap);

    postprocessService.getProcessedData(datadict);

    return new ResponseEntity<>("Job Submitted", HttpStatus.OK);
  }

  @RequestMapping(value = "/ht", method = RequestMethod.GET)
  public ResponseEntity<?> healthcheck() {
	  return new ResponseEntity<>(HttpStatus.OK);

  }

  @RequestMapping(value = "/", method = RequestMethod.GET)
  public ResponseEntity<?> rt() {
	  return new ResponseEntity<>(HttpStatus.OK);

  }
}
