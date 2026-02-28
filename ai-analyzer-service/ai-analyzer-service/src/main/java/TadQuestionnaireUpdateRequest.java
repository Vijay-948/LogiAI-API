package com.peopletech.fractionable.dto.request.tad;

import lombok.Data;

@Data
public class TadQuestionnaireUpdateRequest {
  private Integer id;
  private Integer sjdId;
  private Integer candidateId;
  private String answer;
  private Boolean isSatisfied;
  private String aiFeedback;
}
