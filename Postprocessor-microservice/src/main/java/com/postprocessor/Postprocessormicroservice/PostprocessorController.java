package com.postprocessor.Postprocessormicroservice;

import java.util.concurrent.atomic.AtomicLong;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PostprocessorController {
	
	private static final String template = "Hello, %s!";
	private final AtomicLong counter = new AtomicLong();
	
	@GetMapping("/getcontent")
	public Postprocessor postprocess(@RequestParam(value = "name", defaultValue = "World") String name) {
		return new Postprocessor(counter.incrementAndGet(), String.format(template, name));
	}

}
