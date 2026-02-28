package com.peopletech.fractionable.dto.request.tad;

import com.peopletech.fractionable.dto.UserDetailsDto;
import lombok.Data;

@Data
public class TadApprovalProjectRequest {
  private Integer projectId;
  private Integer clientId;
  private String projectName;
  private UserDetailsDto hiringManagerId;
}
