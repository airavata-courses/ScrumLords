package com.postprocessor.Postprocessormicroservice;


import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
// import org.springframework.cloud.gcp.pubsub.core.PubSubTemplate;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.core.task.TaskExecutor;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

@SpringBootApplication
@EnableAsync
public class PostprocessorMicroserviceApplication {

//   public PubSubTemplate template;

  public static void main(String[] args) {
    SpringApplication.run(PostprocessorMicroserviceApplication.class, args);
  }

  @Bean
  public CommandLineRunner commandLineRunner(ApplicationContext ctx) {
    return args -> {
      System.out.println("SERVICE IS RUNNING!!!");
    };
  }

  @Bean(name = "processExecutor")
  public TaskExecutor workExecutor() {
    ThreadPoolTaskExecutor threadPoolTaskExecutor = new ThreadPoolTaskExecutor();
    threadPoolTaskExecutor.setThreadNamePrefix("Async-");
    threadPoolTaskExecutor.setCorePoolSize(3);
    threadPoolTaskExecutor.setMaxPoolSize(3);
    threadPoolTaskExecutor.setQueueCapacity(600);
    threadPoolTaskExecutor.afterPropertiesSet();
    System.out.println("ThreadPoolTaskExecutor set");
    return threadPoolTaskExecutor;
  }
}
