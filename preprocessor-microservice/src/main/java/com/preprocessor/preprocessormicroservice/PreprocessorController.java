package com.preprocessor.preprocessormicroservice;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class PreprocessorController {
	
	@RequestMapping("/")
		public String index() {
			return "Greetings from Spring Boot!";
		}
	
}
