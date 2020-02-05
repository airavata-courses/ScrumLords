package com.postprocessor.Postprocessormicroservice;

import java.util.Map;
import java.util.concurrent.atomic.AtomicLong;

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
	
	//private static final String template = "Hello, %s!";
	//private final AtomicLong counter = new AtomicLong();
	
	@RequestMapping(value = "/postprocess", method = RequestMethod.POST)
	public ResponseEntity<?> postprocess(@RequestBody Map<String, Object> data) {
		//return new Postprocessor(counter.incrementAndGet(), String.format(template, name));
		//System.out.println(data);
		return new ResponseEntity<Map>(data, HttpStatus.OK);
	}

}
