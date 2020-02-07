package com.postprocessor.Postprocessormicroservice;

import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.gcp.pubsub.PubSubAdmin;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class PostprocessorController {

	@Autowired
	private PostProcessService postprocessService;
	
	
	@RequestMapping(value = "/postprocess", method = RequestMethod.POST)
	public ResponseEntity<?> postprocess(@RequestBody Map<String, Object> data) {
		

		postprocessService.getProcessedData(data);
		return new ResponseEntity<>("Job Submitted", HttpStatus.ACCEPTED);
	}

}
