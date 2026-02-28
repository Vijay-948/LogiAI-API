package com.peopletech.fractionable.dto.request;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class TagCandidateRequest {
  private Integer sjdId;
  private Integer candidateId;
  private String resumeId;
}
