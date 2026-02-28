package com.peopletech.fractionable.dto.request.tad;

import java.util.Date;
import lombok.Data;

@Data
public class TadClientProjectRequestDto {
  private Integer clientId;
  private Integer projectId;
  private String projectName;
  private Date createdOn;
  private Date modifiedOn;
  private Boolean status;
}
