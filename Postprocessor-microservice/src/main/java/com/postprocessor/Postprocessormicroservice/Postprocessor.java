package com.postprocessor.Postprocessormicroservice;

public class Postprocessor {
	private final long id;
	private final String content;
	
	public Postprocessor(long id, String content) {
		this.id = id;
		this.content = content;
		
	}
	
	public long getId() {
		return id;
	}
	
	public String getContent() {
		return content;
	}
}
