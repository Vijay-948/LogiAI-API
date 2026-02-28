package com.peopletech.fractionable.dto.request;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

@Data
@JsonIgnoreProperties(ignoreUnknown = true)
public class SuitabilityScoreResponseDto {
  @JsonProperty("similarity_score")
  private Float suitabilityScore;
}
