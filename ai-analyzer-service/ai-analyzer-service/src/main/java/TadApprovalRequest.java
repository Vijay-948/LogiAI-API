package com.peopletech.fractionable.dto.request.tad;

import com.peopletech.fractionable.dto.LookupDto;
import java.util.Date;
import java.util.List;
import lombok.Data;

@Data
public class TadApprovalRequest {
  private String clientName;
  private Integer clientTypeId;
  private LookupDto clientId;
  private Integer clientUserId;
  private Boolean clientStatus;
  private Boolean approvalRequired;
  private Date createdOn;
  private Date modifiedOn;
  private Integer createdBy;
  List<TadApprovalProjectRequest> projects;
}
