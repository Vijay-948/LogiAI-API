package com.peopletech.fractionable.dto.request;

import lombok.Data;

@Data
public class CandidateSubStatusChangeRequest {
  private Integer candidateId;
  private Integer sjdId;
  private String subStatus;
  private String comment;
}
