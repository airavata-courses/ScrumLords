package com.postprocessor.Postprocessormicroservice;

import java.lang.reflect.Type;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

import org.apache.tomcat.util.codec.binary.Base64;
import org.apache.tomcat.util.json.JSONParser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gcp.pubsub.PubSubAdmin;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.google.cloud.pubsub.v1.Publisher;
import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;



@RestController
public class PostprocessorController {

	
	
	@Autowired
	private PostProcessService postprocessService;
	
	
	@RequestMapping(value = "/process/analyze", method = RequestMethod.POST)
	public ResponseEntity<?> postprocess(@RequestBody Map<String, Object> data) {
		
		Map<String, Object> dataObj = (Map<String, Object>) data.get("message");
		System.out.println("TEST 1");
		//System.out.println(dataObj);
		
		String dataObj2 =  dataObj.get("data").toString();
		System.out.println("TEST 2");
		//System.out.println(dataObj2);
		
		byte[] byteArrayData = Base64.decodeBase64(dataObj2.getBytes());
		System.out.println("TEST 3");
		//System.out.println(byteArrayData);
		String decodedData = new String(byteArrayData);
		System.out.println("TEST 4");
		//System.out.println(decodedData);
		
	
		HashMap<String,Object> datamap = new Gson().fromJson(decodedData, new TypeToken<HashMap<String, Object>>(){}.getType());
		
		Map<String, Object> datadict = new HashMap<String, Object>();
		
		datadict.put("data", datamap);
		
		System.out.println("DATA DICT Created");
// 		System.out.println(datadict);
		postprocessService.getProcessedData(datadict);
		
		
		return new ResponseEntity<>("Job Submitted", HttpStatus.ACCEPTED);
	}

}
