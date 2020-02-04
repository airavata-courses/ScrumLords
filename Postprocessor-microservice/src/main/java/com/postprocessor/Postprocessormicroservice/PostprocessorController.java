package com.postprocessor.Postprocessormicroservice;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PostprocessorController {
	
	@RequestMapping("/")
	public String index() {
		return "Greetings from Spring Boot!";
	}

}
