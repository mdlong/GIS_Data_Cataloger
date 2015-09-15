USE [CMTAGISStats]
GO

/****** Object:  Table [dbo].[Layers]    Script Date: 9/15/2015 6:35:10 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Layers](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[MXD_Name] [nvarchar](100) NULL,
	[MXD_Path] [nvarchar](500) NULL,
	[MXD_ID] [int] NULL,
	[LYR_Name] [nchar](100) NULL,
	[LYR_Path] [nvarchar](500) NULL,
	[LYR_Type] [nvarchar](25) NULL
) ON [PRIMARY]

GO


