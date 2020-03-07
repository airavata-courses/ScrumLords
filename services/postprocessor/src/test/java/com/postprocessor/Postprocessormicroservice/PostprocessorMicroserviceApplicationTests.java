package com.postprocessor.Postprocessormicroservice;


import static org.hamcrest.Matchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

@SpringBootTest
@AutoConfigureMockMvc
class PostprocessorMicroserviceApplicationTests {
	
	@Autowired
	private MockMvc mockMvc;
	
	@Autowired
	private PostprocessorController controller;
	
	@Test
	public void shouldReturnDefaultMessage() throws Exception {
		String content = "{\"subscription\":\"projects/falana-dhimka/subscriptions/post_process_sub\", \"message\": {\"data\":\"\", \"messageId\":\"6\", \"attributes\":{}}}";
		this.mockMvc.perform(post("/process/analyze")
						.contentType(MediaType.APPLICATION_JSON)
						.content(content))
						.andDo(print())
						.andExpect(status().isOk())
						.andExpect(content().string(containsString("Job Submitted")));
	}
	
	@Test
	public void contexLoads() throws Exception {
		assertThat(controller).isNotNull();
	}
}
